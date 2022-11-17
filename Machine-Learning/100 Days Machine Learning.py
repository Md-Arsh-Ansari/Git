                            

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
    Supervised learning: ka fanda ye tha ki Input aur output dono hona chahiye. 
    Unsupervised: ka fanda ye tha ki aap sirf input dete ho.
    "Reinforcement": ka fanda ye hai. ki yaha par aap data dete hi nahi ho. aapke system ke paas koi data hota hi nahi hai. aapka algorithm ekdam scratch se seekhna start karta hai. aur phir dheere dheere improve karta jata hai. kaam karta hai ho gaya to thik usse bhi seekhta hai. ya agar galti hota hai to usse bhi seekhta hai.
    galti karne se usko punishment milta hai. jaise uska marks kat say -50. 
    aur kaam ko sahi karne se usko reward milta hai. say +50. 

galti karta hai. to wo apne system ko khud hi se update karta hai. ki ye kaam ab dubaara nahi karna hai. 
Sahi karta hai. to apne system ko update karta hai. ki aise situation me isi kaam ko karna hai. yahi option ko choose karna hai.
Uska goal ye rahta hai. apne reward ko badhana aur punishment ko ghatana.




-----------------------------------------------------------------------------------------------------------------

                            Day 4: Types of Machine Learning

Based on How the machine learning model train actually. specially on production.

Now, 

Production: What is production. Production is basically the server. where your code is going to run. 

Production environment: and the environment of server where your code is running, is called Production environment. 

development environment: And the machine where you are doing your coding. is called development environment. 


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

Online learning quite unlike batch learning is incremental. You feed your model data in small - small batches, sequentially. These batches are called mini batch. After every training your model improve.
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



-----------------------------------------------------------------------------------------------------------------

                            Day 7: Challenges in Machine Learning
                            

1. Data Collection: While learning you have so many data. data given by your teachers, given on kaggle etc. But while doing your actual machine learning job on a company. Then data collection or data gathering is quite difficult. 
You can fetch data from an API or you can do web scraping. These are the two famous approch.
But on these approch also bahut tarah ke gadbad ho sakte hai. aap doosre ke server se apne machine me data la rahe ho. to is lane ke process me bahut sare problems ho sakte hai.


2. Insufficient Data / Labelled Data: aapke paas data aa bhi gaya to kya wo sufficient hai. aur agar wo sufficient hai to kya wo labelled hai. 
Koi ek algorithm jo bahut acha hai par wo 100 rows of data collect karta hai. aur koi doosra algorithm hai jo utna acha nahi hai par wo 1 millions of data collect karta hai. to aapke liye wo doosre algorithm useful hai.


3. Non Representative Data: Data agar aadha hai aur wo aadha sach bol raha hai ya aadha kahani bata raha hai to aapko wo result galat dega. 


4. Poor Quality Data: aap apna 60% time data ke quality ko sahi karne me gujar dete ho. e.g., outliers, abrupt format me value. 
if your data quality is poor your results are going to poor.


5. Irrelevant Features: Garbage in Garbage out. kis input ko rakhna hai. kis input ko nahi rakhna hai ye decide karna mushkil hota hai. kyuki agar aap garbage input karoge. to garbage output aaega.  


6. Overfitting: agar ML model data ko rat leta hai. wo uske peeche ka concept nahi seekh pata hai. to new data me wo acha perform nahi karega. 
Training data ko leke kuch jyada hi serious ho jata hai. wo insight nahi nikalna jaanta, overview nahi lena jaanta wo bas training data ko hu bahu follow karta hai.


7. Underfitting: Underfitting is just opposite to overfitting. model training data ko seriously leta hi nahi hai. wo bas oopar oopar se dekh ke hi ek opinioun bana deta hai. aur output predict kar deta hai. 


8.  Software integration: Machine learning ko banaya hi isliye jata hai. ki use software me dala jae. lekin har software machine learning ko itna jaldi accept nahi kar paata hai. wo ho sakta hai. windows ka software alag hote hai. mac ke alag aur linux ke alag. aur software jaise agar java ko use kar ke banaya gaya hai. to isme bahut jyada hacking karna padta hai. aur model ko dalna bahut mushkil hota hai. 
islye koshish kare End to End product banane ka. bas ML model bana ke baith nahi jana hai. usko website me ya app me convert kiya jae. 


9. Offline Learning / Deployement: Deployment me bahut cost lagta hai. aur aapko insure karna padega ki aapka model constantly update hote rahe. aur update ke liye Deployement karna hi padega. 


10. Cost involved: agar aap bade scale me koi cheej kar rahe ho. Product bana ke use deploy kar rahe ho. aur daily basis me 10,000 se 1 Lakh user us software ko use kar rahe hai jaha par aapka Machine learning model run kar rahe hai. to bahut saare jagaho aur bahut saare alag alag areas se aapko paise lagne lagenge. Hidden cost lagne lagenge. aur jiske liye companies allow bhi nahi karenge.
Ab aapka task ye hai ki un kharcho ko kam kaise kiya jae. aapko seekhna hai Machine Learning product ko banana aur chalana dono seekhna hai.
MLops: Machine Learning model ko server me daal ko uska kharcha manage karna, Load balancing karna ye sab aur ye aaj ke date me bahut Growing field hai. 



-----------------------------------------------------------------------------------------------------------------

                          Day 8: Application of Machine Learning


B2B: There are so many B2B examples are there. like YouTube pe video recommendation, Facebook pe friend recommendation, amazon pe product recommendation etc.

B2B : Business To Business Machine learing ek product me ghus ke ek business ko help kar rahi hai usko run karne me. 
B2B ki agar baat kare to ye B2C se bahut jyada paisa kamane wala cheej hai.

Machine Learning B2B me kaise Help kar raha hai: 

Retail Sector: Retail me ML bahut jyada use ho raha hai. like Amazon me Sales start hone se pahle Data Analyst, Machine learning engeneer in sab ko bhithaya jata hai aur ye find karne ko kaha jaata hai. ki kin kin products ka humlog ko stock jama karna padega.
Big Bazar: Ask for Phone number. Track karte hai. buying behaviour ko. jaise health wale cheeje aap khareedte ho to ye log categories karte hai ki aap health ko le ke concious ho. aur baad me ye companies is data ko third party ko bech dete hai. aur phir waha se aapko call aata hai ki sir aap gym membership khareed lo etc etc.
kaun sa saman kaha rakhna hai isme bhi ML use hota hai correlation nikal ke ki ye product is product se bahut jyada coreleted hai.


Banking and finance: 
Loan kisko dena hai. kisko nahi ye sab aapke profile ko dekh ke bata sakte hai. ki aap loan chukaoge ya nahi.


Transport OLA:
kis area me driver ka supply bahut kam hai aur ek perticular time me demand bahut jyada ho jata hai. jaise Office ke chuttti hone ke samay. to OLA cab drivers ko map me show kara deta hai. ki is area me jane par aapko 2 X  ya 3 X jyada fare price milega.

 
Manufacturing - Tesla: 
Predictive Maintainence me bahut help karta hai. jaise Tesla me jo automated equipments hai jo car ke alag alag parts ko bana rahe hai unme "IOT" ("Internet Of Thing") dala jaata hai. jo un equipments ke temperature pressure ye sab cheej ko measure karte rahte hai. aur us data ko ek server me bhejte rahte hai. phir Analysis kar ke ingeneers ko bheja jata hai ki jao us machine me gadbadi aa raha hai. aur is tarah machine ke kharab hone se pahle hi usko thik kar liya jata hai. isi ko kahte hai. Predictive Maintainence.


Consumer Internet- Twitter.
eg., Sentiment Analysis: kar ke ye pata lagana ki Narendra modi jeetenge ya mamta banarji jeetengi. 60% tweets Narendra Modi ke favour me hai. aur 40% tweets mamta ke support me hai. to Twitter ye data ab different companies ko bechega. like Stock brokers. aur ab uske paas jitne aadmiyo ka paisa hai. wo un paiso ko le ja ke un companies me laga dega jo BJP ke jeetne par aur oopar jaengi jaise JIO. aur is tarah stock brokers ko profit hoga. twitter ko bhi paisa mil gaya. 


-----------------------------------------------------------------------------------------------------------------

                          Day 9: Machine Learning Development Life Cycle
                          

It is a set of Guideline which you have to follow when you make machine learning based software product.
it will teach you the complete process from idea to Product.


1. Framing the Problem: aap apne college ka project nahi bana rahe ho. ek well trusted company ke liye poora model bana rahe ho. aap launch ke baad ye nahi bol sakte ki nahi isko aisa hona chahiye tha aisa ho gaya, ab isko shuru se badlte hai. 
aapke shuru se last tak har cheej ka Framing karna padega. kharcha kitna lagega, kitne logo ki team chahiye. end product kaisa dikhai dega. aapka jo Model hone wala hai wo Supervised hai. ya unsupervised hai. offline hoga ya batch mode me chalega. data kaha se aaega. is tarah ke saare problem ka solution pahle se ready rahna chahiye. 

2. Gathering Data: from csv, api, web scraping, ya ETL, data kaha se lae aur usko kaha aur kis form me store kare. jaha se ki constantly us data ko access kar sake.

3. Data Preprocessing: Cleaning the data like remove duplicates, handle outliers, scaling, 

4. EDA: input aur output ke bich ka relation nikalne ki koshish. data ke baare me jitna jaan sakte ho jaan lo. aapko bahut saara experiment karne hote hai. aur data ke andar ke relationships ko find karna hota hai. ki we kaise ek doosre se jude hai.
yahi aap graph wagairah plot karte ho. isi step me visualization karte ho. mean, standerd deviation find karna sab isi step me karna hota hai. ye wo step hai jisko kulhadi tej karna kahte hai. kulhadi ko aap jitna jyada tej karoge ped kaatne me utna kam mehnat lagega. 


5. Feature Engineering and Selection: 
input column ko select karna. ki kisko rakhe kisko nahi rakhe taki load na pade. aisa input jisko rakhne ka koi meaning nahi banta hai. usko hatana wagairah.

6. Model Training, Evaluation and Selection: 
khub sare model se check kiye ki is data me kaun sa algorithm acha perform kar raha hai.
final model ko select kar ke aap uske settings ko tune karte ho taki uska performence aur improve ho jae.


7. Model Deployment: apne ML model ko utha ke server me daal dete ho. so that usko website me ya android app me istemal kiya ja sake. 
apne ML model se ek binary file bana lete ho aur API me convert kar dete ho. hum jaante hai ki API me sahi input de to wo palat ke JSON deta hai.
user website me ek input dega. input server me python app ko milega. python API ke paas wo input bhejega. API me aapki wo binary rakhi hui hai. jo apna kaam karega Prediction kar ke. aur yahi prediction ko JSON ke form me user ko dikha dete ho. 
to deploye you use tools like heroku etc.


8. Testing: Apne kuch chuninda aur trusted customer ke paas koi naya feature bhejte ho. aur unse feedback lete ho. feedback positive milta hai to aage proceed karte ho. aur negative milta hai. to peeche ke model ko hi chalne dete ho.

9. Optimize: agar feedback positive mil jata hai. to at scale us feature ko launch karne se pahle kuch steps lete ho jise optimization kahte hai jaise: 
    Model ka backup lena,
    data ka backup lena,
    load balancing
    kharche ko kam karne ki koshish karte ho.etc etc.
    



-----------------------------------------------------------------------------------------------------------------

                         Day 10:  Data Science Job Roles


'Job search engine': AngelList where startups post their jobs.

    Data Engineer
    Data Analyst,
    Data Scientist,
    Machine Learning Engineer, 
    {MLops}


'Various Data Based Job Roles': Saare job roles Machine Learning Development Life Cycle se nikal ke aae hai. kyuki Large scale par Itna bada process ye ek aadmi ke sar pe nahi thop sakte ho.

1.'Data Engineer': 

#Job Roles
Data engineer ka kaam hota hai sara data la kar ek table par de dene ka. so that baki log us data ko use kar pae.

ek sabse important kaam hota hai. DataBase se DataWarehouse banana. aur ye bahut hi specialised kaam hai. isme aapko kafi software ka knowledge hona chahiye. aur databases ka acha knowledge hona chahiye.
Scrape Data from the given sources in a right format.
Build data pipelines/APIs for easy access to the data. Ki API sahi se kaam kar rahe hai ki nahi.
Handle databases/data warehouses. check karna ki databases break to nahi kar rahe hai.

kyuki bade scale me data ko handle kar paana bahut mushkil hota hai.



#skills Required
Ye banda ek aisa banda hota hai jo ek proper software developer hota hai. jisko back end , databases, aur server ka poora knowledge ho. 

Strong grasp of algorithm and data Structure.
Progamming Language (Java/R/Python/Scala)
Advavnced DBMS's' (SQL , NoSQL)
Big Data Tools (Apache , Hadoop , Apache kafka, apache Hive)
Cloud Platforms(Amazon Web Services, Google cloud platforms)
Distributed Systems
System design ka acha knowledge.
Data Pipelines.


Data Engineers ko bahut salary milta hai. uska ek reason ye bhi hai ki jo skills Data Engineers ko chahiye hota hai. wo itna easily nahi mil pata hai. isliye Data Engineers bahut kam hai is domain me. 

This field is related to Data but not related to Data Science. It is for Hardcore Software ingineers. 
is cheej me aap tab ghuso jab aap passionate ho software ko le kar ke. kyuki is task ko bade scale me ek software ka banda hi ache se kar sakta hai.

2. Data Analyst: 

Data Analyst ka ka data ka analysis kar ke Reports banana hota hai. taki log us report ko dekh kar ke aage ke model bana pae.

Responsibility:
Cleaning and organizing Raw data.
Analyzing data to derive insights
Creating data Visualizations
Producing and maintaining reports
Collaborating with teams, and collegues based on the insight gained 
Optimizing data collection procedure

Skills:
Statistical Programming.
Programming languages (R / SAS / Python)
Creative and Analytical thinking(Common Sence).
Business Acumen - Medium to high(let say Agar sports ke domain me ho to us perticular sports ka understanding hona chahiye)
Strong communication skills
Data Mining , cleaning , and munging
data visualization
Data story telling
SQL
advanced Microsoft Excel



3. Data Scientist: 

One line: "A data Scientist is someone who is better at statistics than any software engineer and better at software engineering than any statistician."

Data Scientist is a 'Full Stack' guy. Data Scientist wo banda hota hai jo is 'Machine Learning Development Life Cycle' ka har kaam kar sakta hai.

Analytical Skill ka jaroorat hota hail jisko normally "common sense" kahte hai. 
Data Analyst ka kaam hai, past me dekhna ki kya hua, kyu hua , kaise hua, uska reason kya tha. ye kind of summary dene ka kaam karte hai.

Where as Data Scientist ka kaam hai. data ko samajh kar ke future ke liye kuch banana. ye kind of Predictive analysis dete hai. ki future me kya ho sakta hai.

Your Main goal should be to become a Data Scientist because this is the guy who is the main guy. Data Scientist is a Full Stack Guy.


ek Badi company me Data Scientist Role hota hai. ek end to end 'Model create' karna best performing model create karna.
But 
At a startup or a small company: You will be performing all the roles, may be us company me Data Engineer na ho to aapko Data Engineer ka bhi role play karna padega.


Bahut jagaho par ise "Decision Scientist" bhi kaha jata hai. 
is field me ghusna hai to main goal you should apply for is this "Data Scientist".
Sare Algorithm ka gyan hona chahiye. Maths tagda hona chahiye. Thoda bahut software aana chahiye, analytical skill bahut achi honi chahiye. Communication skill bahut achi honi chahiye. kyuki aapko Data Analyst ke saath baat karni hai. aapko us bande se baat karna padega jo is 'machine learning model ko software me deploye' karega.  



4. ML Engineer: 

ML engineer ka kaam bahut chota sa hota hai. 
ek baar model ban gaya to wo kewal us bane banae model ko website me ya app me deploy karwaega. 

The work of a Machine Learning Engineer is to bridge the gap between Data Scientist’s work and production environment. A Machine Learning Engineer is more concerned with deploying production-ready models. For an example, think of a recommender system machine learning model trained with a data set and has achieved great results, now that model needs to be deployed as part of a company’s website to make the site better and thus, help generate more revenue. But what if that model is not production-ready yet? This is where a Machine Learning Engineer comes into play. Deploying machine learning models to a production-ready environment is an engineering concern that is different from building the model. It involves different types of engineering work such as integrating the model to a software system, optimizing the model for performance and scalability, and re-training it with new data, monitoring, and maintenance the ML system

software ingeener wala banda us Data Science wale bande se baat hi nahi kar paega kyuki dono ki experties alag alag hai. 
So, you need to bridge this knowledge gap. thats why a new job profile comes in "Machine learning Engineer".


kyuki probably Data Scientist ko Software development nahi aata. aur jo software Developer jo hote hai. unko Data Science nahi aata.
 
Responsibility: 
Deploying machine learning models to production ready environment.
Scaling and optimizing the model for production
Monitoring and maintenance of deploying models.

Skills: 
Mathematics
Programming Languages (R/Python/ Java / Scala mainly)
Distributed Systems
Data model and evalution
Machine Learning models
Software Engineering & System design.


Mere hisab se aapko Data Scientist banna chahiye. 
Bahut jyada paisa chahiye. to Data Engineer Ban jao.
Agar aapko bas data ke saath khelna hai. Model wagairah nahi banana hai. bahut jyada Maths me nahi ghusna hai. to Data Analyst ban jao.
Aur kuch nahi bhata hai. to Machine learning Engineer Ban jao.



-----------------------------------------------------------------------------------------------------------------

                         Day 11:  What are Tensors.
                         

Tensor is nothing but a Data structure. Data Structure matlab data ko store karne ka tarika. Means it is a container to store numbers. 

Why we are studieng Tensor First: Because libraries like Scikit Learn, Tensorflow all use Tensor. If you are solving any problem on the field of machine learning or deep learning you would be using tensor.

Vectors and Matrices are also tensor. 
when they have zero dimension. you call them scalar. like a single number. 
Jb list of number hote hai to unko vector kaha jata hai. aur jab 2 Dimension me number hote hai. to unko matrices kahte hai. lekin agar wo 3d me ho to unko kya bolenge. 4d me ho to unko kya bolenge. 
To ye decide kiya gaya ki ek general term decide karte hai. And they called it 'Tensor'.
To 'n dimensional' array ko 'Tensor' kaha jata hai.


2. 0D Tensor / Scalar: 

is tensor ka number of dimension zero hai.


3. 1D Tensor / Vector: 

1D array or simply array. 

no. of axis = rank = no. of dimension

[1, 2, 8, 9]
is example me
    Tensor = 1D hai. lekin
    Vector = 4D hai kyuki jitne number honge wo utne dimension ka vector hoga.



if you want 1D Tensor. which are vector. then you have to add multiple 0D Tensor. means you have to add multiple scalar.

if you want 2D Tensor. which are matrices. then you have to add multiple 1D Tensors. means you have to add multiple vector.


4. 2D Tensor / Matrices:

Vectors: [1, 2, 3]  ,  [4, 5, 6]  ,   [7, 8, 9]

Matrices: collection of vectors.
=
[ [1, 2, 3]
 [4, 5, 6]
 [7, 8, 9] ] 
 
 Dimension is 2D = 1 column axis and 1 row axis.
 
Shape: (3, 3)


      #Tell the shape and no of items of following matrices:
a)     [[1, 2],
       [4, 5],
       [7, 8]] 
       Shape = (3, 2)
       items = (3 x 2) = 6
       
b)      [ [1, 2, 3]
         [4, 5, 6] ] 
         Shape = (2, 3) 
         items = (2 x 3) = 6
       
       

5. ND Tensor :

if you want to make a 3D tensor: 

    and you have 1 matice. which contain 3 rows and 3 columns. means.
    shape of 1 2D tensor/matrice = (3,3)
    then you make more 3 matrices. after making now you have total 4 2D Tensor/matrice in total where every matice contian 3 X 3 arrangement. 
    means 
    4 X 3 X 3 then this would be 3Dimensional Tensor.
    because you have a collection of 2D Tensors.
    which is 4 collection of 2d Tensors/matrices.
    
    shape of this 3Dimesional Tensor example= (4, 3, 3)
    number of item = (4 x 3 x 3) = 36
    
   
    
    
    Lekin machine learning me aap zero se 5D ke beech me hi kaam karte ho.
    
    0D to 5D.
    
     
     1D or 2D Tensor:
    Machine learning me Sabse jyada 1D aur 2D Tensor use hote hai. 
    
     3D Tensor:
    3D tensor ka use  'NLP' me aur 'Time series' me hota hai. Time Series ka use stock market me aur medical ke field me bahut hota hai.
    
     4D Tensor:
    4D Tensor ka bahut badhiya use hai. Image based data. and field is called "Computer Vision (CV)". 
    
    
    5D Tensor: 
    Collection of Videos is a 5D Tensor.
    
    
    

-----------------------------------------------------------------------------------------------------------------

                         Day 14 :  Framing a Machine Learning Problem
                         

1. "Business Problem to ML Problem": 

eg., Netflix. me revenue ko increase karne ke liye ek upay ye nikale ki company ke churn rate ko ghatana hai. "Churn Rate" matlab no. of customers jo company chor kar ja rahe hai. us number ko ghatana hai. 
wo churn rate present time me agar 4% hai. to usko ghata ke 3.75% me lana hai. 
To ab aapka focus is par nahi hai ki aapko netflix ke revenue ko increase karna hai. ab aapka focus aur aapke poore team ka focus sirf is baat par hai. ki company ke churn rate ko 4% se ghata kar 3.75% me le ke aana hai. 
Kabhi bhi aapko koi problem mile aapka first instinct as a Data Scientist should be ki mai us problem ko ek mathematical problem me kaise convert kar sakta hu. 
is case me aap ye revenue increase karne ke problem ko ek mathemetical problem me is tarah se change karoge ki aap apne teammate ke paas jaate ke saath bol sakte ho ki "Hamare next 6 month ka target hai. churn rate ko 4% se ghata kar 3.75% tak le aana."



2. "Type of Problem": 

aap ye identify karne ki koshish karte ho ki aap kis type ka problem solve karne ki koshsish kar rahe ho. like - supervised or unsupervised, supervised hai to regression hai ya classification hai. etc. 
aapko bigger picture assume karna hai. 
e.g., aapko ab churn rate churn rate nahi karna hai. aapko ab dekhna hai. ki churn rate kis cheej se infuence ho raha hai. means you have to identify the costemers who are going to leave the platform. 
then aap har chor kar jane wale bande ki probability nikaloge ki is bande ke platform chor kar jaane ki probability itni hai . aur iski itni hai. 
to jis bande ki probability jitni high hai. usko utna discount de kar rokne ki koshish karni hai. 

to ab kisko kitna discount dena hai. uska pata lagane ke liye hum Classification ke bajae ab Regression ko select karenge ki ye problem jo hai. ye ek Regression ka problem hai.



3. "Current Solution":  

is problem ke kuch existing solution pahle se hoga hi jiska use company me kiya jaata hai. kyuki ho sakta hai. pahle bhi koi team is problem me kaam ki hogi to aap ja ke us team se baat kar sakte hai. ki is problem ko solve karne ke liye aapne kya kiya tha? hum ye karne ki soch rahe hai. aapki kya rai hai iske baare me. jo solution hai usko aapne kya soch kar banay tha kin kin cheejo ko dhyan me rakhte hue is solution tak aae the aaplog. to agar wo solution helpful hai to usko pakad ke usi direction me kaam karna aasaan hota hai. aapk zero se start karne se bach jaate ho. 


4. "Getting Data": 

kaun banda platform chor kar jaega. isko predict karne ke liye kuch data gather karna padega costemer ka ki:

    1. Watch time (kitna hai. bande ka)
    2. Search but did not find (search kiya movie par nahi mila)
    3. Content left in the middle (aadhi film dekh kar chor diya)
    4. Clicked on Recommendations(Order of Recommendations)



5. "Matrices to Measure": 

AAp jo predict kar rahe the aap sahi the ki nahi isko pata karne ke liye aap ek matrice set karoge jisko measure kar ke insure ho sako ki aap jis direction me badh rahe ho wo sahi hai.     
    
    
6. "Online Vs Batch": 

ye select karna ki Online Learning karoge is problem ko solve karne ke liye ya Batch learning.  



7. "Check Assumption": 

Ye check karna ki aap jo facility assume kar ke chale ho ki aap iska use karoge, iska use karoge. jaise :
    Search but not found
    watch time 
    etc etc. 
    
            Ye sb measure karne ka facility company me available hai. bhi ki nahi. in saari cheejo ko check kar ke ensure karna. aur confirm karna. 
            ye bhi ensure karna ki ye factor globally applicable hai. ya sirf ek country me vary kar rahe hai. ya karenge. 
            
            
            

-----------------------------------------------------------------------------------------------------------------

                         Day 16 :  Working with JSON/SQL


JSON : Java Script On Notation. it is an universal file format means all programming languages support JSON file format. Thats why it is important.

SQL: apne dataframe se directly agar pandas ke madad se import karte hai. to wo SQL format me hota hai. 


PHP seekhna 




 
-----------------------------------------------------------------------------------------------------------------

                         Day 17 :  Fetching Data From an API
                         
                         
Agar kisi website se data fetch karke lana hai to wo kaise karte hai. 


"API": What is an API:
    
    API 2 softwares ko aapas me baat karata hai.
    API data pipelines hote hai. jo information ko point A se point B tak pahuchate hai. 
    
    e.g., Agar hum 'makeMyTrip' se train ka ek seat book karte hai. to wo seat 'yatra.com' me bhi booked dikhai dega. kyuki ye sare website ek official website ka API use kar rahe hai. official ticket book karne wala website apne data base ke charo taraf ek code likh ke rakha hai. kuch function bana diye hai. agar us function ko correct input ke saath likh ke request bheja jae to us official website se palat ke ek jawab aaega jo JSON format me hoga. jo ye bataega. ki Seat khali hai, ya book ho chuka hai.
    
    Questions got resolved in this lecture: 
    #API se data Fetch kaise karna hai.
    #us JSON format ke data ka overview kaise dekhna hai.
    #us JSON format ke data ko kaise ek DataFrame me convert karna hai. 
    #data agar multiple pages me hai. to usko for loop laga ke kaise complete dataFrame ko apne notebook me lana hai. 
    #us DataFrame ko kaise "csv" file me convert karna hai. 
    #us CSV database ko kaise kaggle me upload karna hai.
    #apne kaggle profile ko kaise boost kare uske liye rapid Api ke baare me bataya gaya hai.
    #
    
    
                         
            -----------------------------------------------------------------------------------------------------------------

                         Day 18 :  Fetching data using Web Scraping          
                        
Web API se data fetch na kar sake to Web Scraping ka madad lena padta hai.



    # request bhejne par 200 nahi aaya to kya kare.
    # 4 cheeje ek hi class me hai to unko alag alag kaise print kare.
    # data jo milega usko dataframe me kaise badle. jaisa kaggle me dikhai deta hia.
    


-----------------------------------------------------------------------------------------------------------------

                         Day 19 :  Understanding Your Data


    1. "Asking Basic Questions": What are the basic questions you should ask after getting your data.
            full document on github "day 19 document".
            
            head ke jagah me sample likhe hai taki 5 random data show ho.
            
            df. describe() se jo insite milenge wo kewal numerical data ke bare me janne ke liye valuable hai. 
            
            Correlation : Correlation ka matlab hota hai. ek cheej ke badhne ya ghatne se kisi doosre cheej par kya asar padta hai. 
         
            saare column useful nahi hote hai. jo column useful nahi hota hai. usko identify kar ke column ko hatana ek bahut jaroori process hota hai.
            
            is step me yahi karte hai. kaun sa input column. output column par asar nahi daal raha hai. aur agar daal raha hai to kitna daal raha hai. 
            kya wo directly proportional hai ya inversly proportional hai. 
            
            e.g., Titanic dataset me "Survived" ka "Fare" ke saath ek positive corrilation dikhata hi. "Fare" ke badhne se "Survival" ka chance badh raha hai. 
            
            ab "Pclass" ek storng negative corrilation dikha raha hai. "Survived" ke saath. class 1 sabse jyada survive kiye. aur '3rd' class ke log sabse kam survive kiye. to "Pclass" ke badhne se "survival" ka chance kam ho raha hai.
            
            passenger id me bahut kam value aaya hai to uska koi use nahi hai. us column ko hata dena hi behtar hai.
    
    
    
-----------------------------------------------------------------------------------------------------------------

                         Day 20 :  EDA using Univariate Analysis
                         

1 column ka analysis karna. matlab har column ke oopar independent analysis ko univariate analysis kahte hai. 

1. humko categorical data wale column me apna analysis perform karna hoga. to Sabse pahle ye pata karna hai. ki koun se column me categorical data hai. jaise : class, "survived" etc.
 aur kaun se column me numerical data hai. ya kaun se categorical data wale column hai. ya kaun sa categorical to hai par hamare kaam ka nahi hai. jaise : "name" wala column. 
 
 
 
-----------------------------------------------------------------------------------------------------------------

                                 Day 22 :  Pandas Profiling   
             
EDA using Univariate Analysis aur bivariate ya multivariate analysis wale sare analysis sirf ek peice of code se ho sakta hai. Library is called Pandas Profiling.

Average record size in memory : har ek row kitna size le raha hai memory me.

Name variable has high cardanility: Name variable categorical data hai. jisme category bahut jyada hai.

Yaha par 
"Variables" Tab               = "Univariate Analysis"
"Interactions" and "corrilations " = "Bivariate Analysis"

"count" bateaga ki har column me kitni missing values hai.

"koi bhi ek dataset uthao aur is tool ko run kar do. aur phir jo output report aa raha hai usko padhne ka try karo. aur padhne ke saath saath us observation ko note kar sakte ho. Ye kaam 3 se 4 datasets ke saath karte karte eventually You will become comfirtable with this tool and than you can use this tool in a powerfull way. " 

    
    
-----------------------------------------------------------------------------------------------------------------

                             Day 23 :  What is Feature Engineering 
    
#Aage ke 8 se 10 video me yahi saare topic ko ek ek kar ke padhaya jaega.

Feature engineering is the process of using domain knowledge to extract features (characteristics, properties, attributes) from raw data. These features can be used to improve the machine learning algorithms.


Feature Engineering Types: 

    Feature Transformation 
    
    Feature Construction

    Feature Selection

    Feature Extraction
    
    
    1. "Feature Transformation : 
    koi input column ko transform karna taki aur behtar result de.
    
        i) Missing Value imputation: Missing value ek bada problem hai. kyuki Scikit Learn missing value accept nahi karti hai while training a model. so before either you have to remove them or you have to fill them.
        
        ii) Handeling Categorical Values: Categorical value jo ki String hai. to un String variable ko numerical value me convert kar dena via onehot incoding or some other techniques. 
        
        iii) Outlier Detection: There are certain algorithms jo bahut jyada impact hote hai. outliers ke karan. to pahle un outliers ko detect kar ke romeve karna.
        
        iv) Feature Scaling: koi input variable me data 100 ke under hai. aur kisi me "Lakh" se oopar hai. to apne algorithm ko data dene se pahle features ko Scale kar dete ho. aur ek range me le aate ho jo jenrally -1 se 1 ke beech me hota hai.


    2. "Feature Construction: 
    Data me koi feature exist nahi karte. unko manually construct karna. taki aur behtar result aae. jaise Tatanic dataset me : 'Parent Child' aur 'SiblingSpouse' ko add kar ke ek naya column construct kar diye. 'Family' naam se aur usme in dono ke number ko add kar ke ek kuch aur category bana diye jaise: 'Alone, small family, large family' etc. 
   

    3. "Feature Selection: 
    Saare ke saare feature. saare ke saare column ko algorithm ko nahi de rahe ho kuch ko hata le rahe ho. jo utne jaroori nahi hai.
    jaise 'Mnist' dataset me handwritten numbers ke picture ko detect karne ke liye. sirf centre ke area me focus karna. periferal ke portion ko consider hi nahi karna. taki algorithm ko bahut jyada kaam na karna pade . kewal jaroori kaam par hi focus kare.

    4. "Feature Extraction:
    Given feature me se completely nae feature ko extract karna but programmetically not manualy via using some algorithm.
    
    aapke paas jo given input hai. unke badle aap complete nae features create karte ho. jaise aapke paas 5 feature the. to aap 5 aur nae feature create karte ho. aur un 5 nae feature me se kewal 2 sabse important feature ko use karte ho. aur baaki 3 ko hata dete ho.
   algorithms like PCA, LDA. 
    
    
-----------------------------------------------------------------------------------------------------------------

                           Day 23 :  Feature Scaling   
    
Feature Scaling is the last thing you will do in Feature ingineering part. Machine learning Algorithm ko apna data dene se just pahle aap Feature Scaling karte ho.

It is one of the easiest step in Feature ingineering.

what is Feature Scaling: 
Feature Scaling is a technique to standardize the independent features present in the data in a fixed range. 
    
    eg., iq agar 100 ke range me hai. aur CGPA 10 ke range me hai. to Feature scaling ke baad ye same range me aa jate hai.
    "kyuki agar independent variable ka scaling ache se nahi hoga to Machine Learning algorithm ka Logic is tarah se created hai. ki wo ache se perform nahi kar paenge."
    
    Types of Feature Scaling: 
    
    1. Standardization
    2. Normalization
    
    
    
    1. Standardization: 
    Also called Z-score Normalization. formula : "X – μ / σ"
    Where:  X: the observation (a specific value that you are calculating the z-score for).
            Mu(μ): the mean.
            Sigma(σ): the standard deviation (Data ka spread)
            
       Characteristic: 
        Ye sab karne ke baad jo nae value aaeng unke series ka:
            mean (μ) = 0 hoga.
        aur Stardard deviation (σ)(data ka spread) = 1 hoga.
        
        Standardization me sirf 2 hi cheeje hoti hai: 
        
            1. Mean centering
            2. Scaling by the factor of Stardard deviation which is 1.
            
            
            
            Feature Scaling se pahle (before Normalization or Standardization) : 
            
            1. Train test split kar lena chahiye.(recommended)

    Standardization: 
    
    """from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()""" Sklearn ka ye cheej khud se formula apply kar ke standardize kar degi.
    
    Kaggle me "Learn_Standardization" naam se ek Notebook bana hua hai. usme ye sb show kiya gaya hai.
    
    
    
-----------------------------------------------------------------------------------------------------------------

                           Day 24 :  Feature Scaling - Normalization | MinMaxScaling | MaxAbsScaling | RobustScaling   
                           
   
   Normalization is a technique often applied as part of data preparation for machine learning. The goal of normalization is to change the values of numeric columns in the dataset to use a common scale, without distorting differences in the ranges of values or losing information.                        
    
    "Units ko eliminate kiya jae, so, that Magnitude ko common scale me laya ja sake."
    
    
    1. MinMax Scaling : The min-max normalizer linearly rescales every feature to the [0,1] interval.

Rescaling to the [0,1] interval is done by shifting the values of each feature so that the minimal value is 0, and then dividing by the new maximal value (which is the difference between the original maximal and minimal values).

The values in the column are transformed using the following formula:

normalization using the min-max function
    
    
    3. Robust Scaling: 
    
    When to use Standardization and when to use normalization. 
    
    
    
    
    
    
    
    
    
    



