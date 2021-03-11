from ..models import Loan
from datetime import *

#Search for loans by a given filter
def filterLoans(filter):
    loans =  Loan.objects.filter(**filter)
    return loans

#Check for a given client if there are any book with delayed delivery
#if it exists, calculate the daily fee and mulct and persists 
#in the field mulct on the loan table
def updateLoanMulct(filter):

    loans = filterLoans(filter)

    #the amount charged for borrowing the book is 
    #the basis for calculating the mulct and daily fee
    base_mulct = 10

    #Update the mulct value
    for loan in loans:

        #The date expected for the return of any book, is 3 days after the loan date
        date_expected_return = loan.date_loan.date() + timedelta(days=3)
        date_today = datetime.today().date() 
        
        #The difference in days of the date expected to the return of a book and the current date
        date_diff = (date_today - date_expected_return).days
        
        if date_diff > 0:

            loan_cost = 10
            total_mulct = 0

            #Checks the number of days of delay, to calculate the value of the mulct
            if date_diff <= 3:
                total_mulct = loan_cost * (3/100)
            elif date_diff == 4 or date_diff == 5:
                total_mulct = loan_cost * (5/100)
            elif date_diff > 5:
                total_mulct = loan_cost * (7/100)

            #The new value charge for loan, is the basis loan cost plus the mulct
            loan_cost += total_mulct

            #Calculates the daily fee
            for day in range(0, date_diff):

                if day <= 3:
                    total_mulct += loan_cost*(0.2/100)
                    loan_cost += loan_cost*(0.2/100)
                elif date_diff == 4 or date_diff == 5:
                    total_mulct += loan_cost*(0.4/100)
                    loan_cost += loan_cost*(0.4/100)
                elif date_diff > 5:
                    total_mulct += loan_cost*(0.6/100)
                    loan_cost += loan_cost*(0.6/100)

            #updates the value of the mulct
            loan.mulct = round(total_mulct, 2)

            #saves the new value of the mulct
            loan.save()


    