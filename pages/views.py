from django.shortcuts import render
from .models import *
from django.db import connection
# Create your views here.
def home(req):
    books = Book_Master.objects.all()
    #  for b in books:
    #       chapters = Book_Chapter.objects.filter(book_id=b.id)
    #       bookChap(b.id)
    context = {'books':books}
    return render(req, 'index.html', context)

def bookDetail(req,bookName):
    book = Book_Master.objects.get(book_name = bookName)
    bookid = book.id
    chapList = bookChap(bookid)
    books = Book_Master.objects.all().exclude(id=bookid)[:5]
    context = {'chapList':chapList, 'book':book , 'books':books}
    return render(req, 'bookDetails.html', context)

def chapDetail(req,bookName,chapSeq):
    book = Book_Master.objects.get(book_name = bookName)
    bookid = book.id
    chap = Book_Chapter.objects.get(book_id=bookid,chapter_sequence=chapSeq)
    context = {'book':book, 'chap':chap}
    return render(req, 'chapter.html', context)


def bookChap(book_id):
     with connection.cursor() as cursor:
        col_names1 = []
        data1 = []
        try:
            cursor.execute('begin')
            cursor.execute("select bookchap(%s,'curs');", [book_id])
            
            #cursor.execute("FETCH ALL FROM 'cur'")
            #cursor.execute('commit')
            row = cursor.fetchone()
            cursor.execute(f'FETCH ALL IN "{row[0]}"')
            result = cursor.fetchall()
            #desc = cursor.description
            return result
            '''
            for column in desc:
                col_names1.append(column.name.title())
            '''
            # for row in result:
            #     '''
            #     temp_dict = {}
            #     for i in range(0, len(col_names1)):
            #         temp_dict[col_names1[i]] = row[i]
            #     data1.append(temp_dict)
            #     '''
            #     print(row)
        except Exception as ex:
            print("EXCEPTION: ", ex)
            data1 = []
            pass