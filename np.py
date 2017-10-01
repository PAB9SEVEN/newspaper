import newspaper
import time
print "Do you want to read the latest news"
print "\n"
print"1)To continue to read the paper\n2)To exit"
user_choice=input("Enter your choice")
if(user_choice==1):
    time.sleep(5)
    print "You can get many languages"
    print "Following are the languages"

    print newspaper.languages()
    news=raw_input("Enter the excat name of the paper you need to read")
    urls=('http://'+news+'.com')
    paper=newspaper.build(urls)
    print "Choose:"
    print "1.Articles \n2.Summary \n3.Category"
    user_input=input('enter your choice')
    if(user_input==1):
        print paper
        count=1
        for article in paper.articles:
            print str(count) +')'+str(article.url)
            count=count+1
        no=input('enter the index of the article to be read')
        article=paper.articles[no]
        article.download()
        article.parse()
        print article.authors
        print article.text
    elif(user_input==2):
        print('enter the index of which you need the summary')
        count=1
        for article in paper.articles:
            print str(count) +')'+ str(article.url)
            count=count+1
        no=input('enter the index of the article to be read')
        article=paper.articles[no]
        print article.title
        print '\n'
        print article.summmary

         
        
    else:
        for category in paper.category_urls():
            print category

else:
    exit()
