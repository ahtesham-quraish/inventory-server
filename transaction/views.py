
from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.models import Category, Bank
from transaction.serializers import TransactionSerializer
from customer.models import Customer
from rest_framework import generics, permissions # new
import traceback
from django.db import transaction

class TransactionView(APIView):
    def get(self,request):
        transactions_set = Transaction.objects.all()
        return Response(TransactionSerializer(transactions_set, many=True).data)

    def post(self, request):
        category = request.data.get('category')
        bank_account = request.data.get('bank_account')
        customer_id = request.data.get('customer')
        inputs = request.data
        categoryData = None
        customerDate = None
        category_instance = Category.objects.filter(id=category)
        if category_instance.exists():
            categoryData  =  category_instance[0]

        if customer_id is not None:
            customer_instance = Customer.objects.filter(id=customer_id)
        else:
            customer_instance = Customer.objects.filter(id=2)

        if customer_instance.exists():
            customerDate = customer_instance[0]
        bank_instance = Bank.objects.filter(id=bank_account)

        print("category input is ======(()((_()())))========", categoryData)
        print("customer input is ", customerDate)
        print("bank input is ", bank_instance[0])
        print(request.data.get('amount'))
        try:

            with transaction.atomic():
                Transaction_Inctance = Transaction.objects.create(category=categoryData,
                                                          customer=customerDate,
                                                          description=inputs.get('description'),
                                                          amount=inputs.get('amount'),
                                                          type=inputs.get('type'),
                                                          invoiceId=inputs.get('invoiceId'),
                                                          date=inputs.get('date'),
                                                          isSuperAdmin=inputs.get('isSuperAdmin'),
                                                          bank_account=bank_instance[0],
                                                          )
                return Response({"status": status.HTTP_201_CREATED})

        except:

            traceback.print_exc()
            return Response({"status": status.HTTP_500_INTERNAL_SERVER_ERROR})


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class CustomerTransactionDetail(APIView):
    def get(self,request):
        cust_id = request.GET.get('cust_id')
        if cust_id is not None:

            if cust_id:
                transactions_set = Transaction.objects.all().filter(customer=cust_id)
                return Response(TransactionSerializer(transactions_set, many=True).data)


# Create your views here.
