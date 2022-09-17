                            

-----------------------------------------------------------------------------------------------------------------

                            Day 2: AI vs ML vs DL

'AI' : Main task of AI is Pattern Recognition, which was expert in Expert system. and was previously AI was equal to expert system. expert system: an expert system was used like an expert of chess game used to code nearly all possible outcome into a program using if else.
But AI was failing in some area when it was using expert system. like it used to fail in image recognition, voice recognition etc. because it was not possible to code in if else all possible outcome of dog breeds or all possible meanings of a voices.
Thats where Machine Learning came into the field. and solved this problem. 

'Machine Learning': Machine is a computer science field where you use statistical technique to find pattern and learn that pattern in your data. The main differnce in machine learning and symbolic ai or expert system is that you dont have to do explicit programming in machine learning. explicit programming means rule based programming where you code line by line for every logic or every possible outcome. 
Instead you feed a data to your system. and your system finds patterns in your data and write rules for the pattern recognition and learn pattern through that data. so, that when system get new data they will find patterns in that data.

"Deep Learning": There is a peak came in recently though in around like 2012. Deep Learning is a Machine Learning. Same procedure same process. feeding data like train data. test data. and you predict pattern. The only difference is that the algorithm used by deep learning is a advance algorithm because it is inspired with our biology, biology of a human. inspired with our neuron. The core unit of Deep learning is based on biological neuron.
Its performence increases when you add multiple layers of neuron. the performance and intelligence of system will increase as you increase the number of layers of neuron.
Its performence increases and increases as we feed it data. The more we feed it data. the more its performence increases. While in machine Learning it also increases with the amount of data we feed to the system. but it increases for a certain limit. when it reaches a limit. after that its performance and intelligence cant be increased. And this is the main reason why Deep Learning comes in and why we need Deep Learning. 
On big data Deep Learning is better but for a limited amount of task and data you don't use Deep Learning. 
    #Aap sui ko use karne ke jagah Talwar nahi use kar sakte ho. aap wo use nahi karoge. aapko ek kabootar ko jibah karna hai. aap talwar bhi use kar sakte ho. lekin aapka kaam ek chote se chaku se hi ho ja raha hai to aap utne bade cheej ko kyu use karoge."


-----------------------------------------------------------------------------------------------------------------

                            Day 3: Types of Machine Learning

Based on amount of supervision Needed we can divide our Machine Learning Algorithm:

    1. Supervised ML
    2. Unsupervised ML
    3. Semi Supervised ML
    4. Reinforcement ML

1. "Supervised ML" : if you have input and output. and you want to find relationship b/w input and output. So, that you could tell or predict the output for a new input. Then this learning is called Supervised Machine Learning. You will do Supervised ML the most, amongs all the types of ML.

    a) Regression: if your output is in numerical form. e.g., How many dogs are present.
    b) Classification: Your output would be categorical. e.g, is Dog is present. Yes or NO.




2. "Unsupervised ML": There are lot of operations. will be using Unsupervised ML.
    a) Clustering : Clustering algorithm could detect which data fall from which group. and it would group that data into different groups.
    b) Anomaly : It would detect outliers and remove that outliers
    c) Dimensionality reduction: it reduces the dimensions or colums of data itelligently to make algorithm more efficient.
    d) Association Rule learning.: it would find association and relation between data.




3. 'Semi Supervised ML':
 It is partially supervised and partially unsupervised. it Helps in Labelling. output is called lebel. e.g., Dog tha ya nahi. ye kon bataega. Human bataega. aur is cheej me cost bahut lagta hai. You could scrape so many input but you have to bring human effort in making output. like scrape so many images of dogs for free this is input. but ek banda chahiye hoga. ye batane ke liye ki is image me kya hai. isko kahte hai output. isko lebal karna padta hai. aur isme human effort lagta hai.
par is Semi Supervised ML ke madad se hum ek ya do ko lebel karte hai. aur baaki sab autometically lebal ho jata hai.
e.g., Google photo ek app hai jisme ye har photo ko alag alag catogary me divide kar dega. jaise is chikne ladke ke photo ko alag(Arsh), is bache ke photo ko alag(Zihan), is aadmi ke photo ko alag jiska much bhi hai aur dadhi bhi hai(Abbu). Ye "Clustering" ka example hai.
    Ab wo us dadhi wale aadmi ke photo ko saamne laega aur poochega ki ye kaoun hai. AAp bata doge ki ye "Abbu" hain. to wo us dadhi mooch wale aadmi ke group ke saare photo ko label kar dega "Abbu" se. to ye Semi Supervised ML. ka example hai.



4. 'Reinforcement ML': 
Supervised learning ka fanda ye tha ki Input aur output dono hona chahiye. 
Unsupervised ka fanda ye tha ki aap sirf input dete ho.
Reinforcement ka fanda ye hai. ki yaha par aap data dete hi nahi ho. aapke system ke paas koi data hota hi nahi hai. aapka algorithm ekdam scratch se seekhna start karta hai. aur phir dheere dheere improve karta jata hai. kaam karta hai ho gaya to thik usse bhi seekhta hai. ya agar galti hota hai to usse bhi seekhta hai.
galti karne se usko punishment milta hai. jaise uska marks kat say -50. 
aur kaam ko sahi karne se usko reward milta hai. say +50. 

galti karta hai. to wo apne system ko khud hi se update karta hai. ki ye kaam ab dubaara nahi karna hai. 
Sahi karta hai. to apne system ko update karta hai. ki aise situation me isi kaam ko karna hai. yahi option ko choose karna hai.
Uska goal ye rahta hai. apne reward ko badhana aur punishment ko ghatana.




-----------------------------------------------------------------------------------------------------------------

                            Day 4: Types of Machine Learning

Based on How the machine learning model train actually. specially on production.

Now, 

Production: What is production. Production is basically the server. where your code is going to run. and the environment of server where your code is running, is called Production environment. And the machine where you are doing your coding. is called development environment. 


Two Types: 

    1. Batch Learning
    2. Online Learning


    1. Batch Learning : 
Batch learning is the convnetional way of training a machine learning model. where you are using all your data at once and utilize all yourr data to train the machine learning model. 
You utilize your whole data to train the model. Data is generally so big. It as big as it could not trained on server. because it is costly and time taking. 
You train the model offline. on your machine. and when the model is trained. you deploy your trained model into production. 
e.g., You train your movie recommedation model in your machine. and then deploy or place this model into server. 

But the problem here is that your movie recommendation model should update every week. in order to recommend properly. because platforms like netflix launch a new movie every week. It will not work on new movies. 
or your spam detection model could not detect spam. because people who send spam mails. find new ways and new keywords to spam. where your model fail to identify those spam mails. 
So, in Batch learning you have to retrain your model every time by yourself by identifying those kind of keywords. and by updating new movie names and videos. So, you have to do this intire things periodically. 

So, here you dont train it online. instead of it, You pull down your entire model. You retrain it with new data. by merging new data into that old data. and then you put the model on server. again and again.

Disadvantage: 
    1. Lots of Data. : if you have lot of data. the training would be very difficult. Your code would break every time.

    2. Hardware Limitation: If you cant connect with internet you could not pull the model. in case you have to update it. So, have to be always connected to the internet.

    3. Availability: You could update it on minimum 24 hrs. you cant update it in less than 24 hrs of time.



-----------------------------------------------------------------------------------------------------------------

                            Day 5: Online Machine Learning


    2. Online Learning: 
company promotions lines like: The performence of our products will increase as you use our product. The more you use it the more its performence increases.
Then the company is using online Learning on their product. 

Online learning quit unlike batch learning is incremental. You feed your model data in small - small batches, sequentially. These batches are called mini batch. After every training your model improve.
This is called online Learning because your model is getting train on server or on production or when you are online. 

You start with few data. and feed it to your machine. and send that on server. and on server you are continuously getting new data.
And now your model is working on two task. It is doing its prediction on new data. and simultaniously learning also. 
e.g,. Alexa, YouTube, 


'When to use?': 

    1. where there is a concept drift
    2. Cost effective: online learning is "cost effective".
    3. Faster Solution.
    
    
"How to Implement":

    Use SGD Regression instead of Linear Regression.
    Use River Python library which works on "Streaming Data or Live data".
    
    
"Learning Rate": 

    It is a tricky thing and very important thing and it is very risky thing.
    
"Out of Core Learning": 

    if you have 50 GB data and you have only 8 GB of RAM.
    It convert this gaint data into small pieces of data.
    

"Disadvantage": 

    'Very tricky to use'.: It is new hance it is very difficult to get what are you expecting out of it.
    'Risky' : It is dependent on "incoming data". and if someone have control over incoming data. then it become Very risky.
    
    

-----------------------------------------------------------------------------------------------------------------

                        Day 6: Instance Base vs Model Based Learning


Learning Types: 

    1. Memorizing 
    2. Generalizing (Concept samajhna, underlying principle samajhna)
    
    
1. "Memorizing": 
there are some ML algorithm which memorize the data. this is called "Instance Based learning".


2. "Generalizing: 
Some ML algorihtms try to understand the underlying principle behind that given data. This type of learning is called "Model Based Learning".


#On future you just have to find out: Wheather this algorithm is using Instance based learning or model based learning.


"Instance Based learning": eg., KNN, RBF networks. input/training data must be kept since each query uses part or full set of training observations. if training data is large like for 1GB it store it so may be high storage require. it is Lazy learner.

"Model Based Learning": Most of the machine learning model use this approch of finding a mathamatical relationship bitween an input and an Output. Can throw away input/trianing data after model training. Low storage require. 
eg., Linear regression, Logistic regression, Decision trees.





    










