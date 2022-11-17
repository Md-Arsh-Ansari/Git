Data Analysis: Data analysis is a process of inspecting, cleansing, transforming, and modelling data with the goal of discovering useful information, informing conclusions, and supporting decision-making.

Process of Data Analysis: 

    1. Asking the right questions
    2. Data Wrangling
    3. EDA
    4. Drawing conclusions
    5. Communicating Results.
    
    
1. Asking Questions: in this step there will be two scenario. 
    The first scenario would be you have given the data and also you have given some questions to find out their answers.
    The second scenario would be you have given the data but you have not given any sort of question or problem to find out their answer or solution. you will be given some open ended problem like "this is the data of our company. analyse it and tell us how will become profitable by the next year."
    So, in this case you have to ask questions by yourself. and question would be something like :
    
    # What feature will contribute to my analysis.
    # What feature are not important.
    # Which of the feature have strong corrilation.
    # Do i need data preprocessing.
    # What kind of feature manipulating/engineering is required.
    
1. Asking the right questions
  
    #. Subject matter expertise.: ipl, banking system.
    #. experience
    
    
2. Data wrangling: 
    Data wrangling—also called data cleaning, data remediation, or data munging—refers to a variety of processes designed to transform raw data into more readily used formats. The exact methods differ from project to project depending on the data you’re leveraging and the goal you’re trying to achieve.
    Steps:
    # Gathering Data:  csv, API, web scraping, database
    # Assessing Data: 
            in this step, the data is to be understand more deeply. before implenting methods to clean it, you will defenitely need to have a better idea about what the data is about.
            finding no. rows & column -shape(), data type & missing value memory occupy -info(), uniqueness -is_unique, mathemetic overview -describe.
    # Cleaning Data.
        missing data (rakhna hai, ya hatana hai, ya replace karna hai. (mean, median, mode se)
        if duplicate (Removing duplicate data by drop_duplicates)
        incorrect data type( astype )
        
    #Types of unclean data: 
        1. Dirty Data: Low quality data. therefore it has content issue.
        2. Messy Data: Messy or untidy data. it has structural issue.
           
    1. Dirty Data: 
        Duplicate Data
        Missing Data
        corrupt Data
        inaccurate Data
        
    2. Messy Data:
        Tidy data has the following quality: 
            # Each variable forms a column.
            # Each Observation forms a row.
            # Each Observational unit forms a table.
            
            if your data violates any one of the above is known as Untidy Data. 
     
     Ab is Dirty Data aur Missing Data ko dhundhne ke 2 tarike hai. 
     
     #There are Two kinds of Assessment style you can do:
        1. Manual: Looking at data manually through google sheet. (jitne bhi students jinka Data Analysis bahut strong hai. unme ek common cheej hota hai. wo log data ko manually ghanto dekhte hai. data ko bas screen par rakh kar dekh rahe hai. nothing else.)
        2. Programmetic: By using pandas functions  like info(), describe() or sample().
        
in assessment ko kar rahe hote ho to aapko do steps follow karne padte hai. 

    #Steps in Assessment: 
        1. Discover: Dhoondhna hai. 
        2. Document: kuch mile to usko kahi par likhte jaana hai. usko document karna hai.
        
    # Data Quality issue are divided into 4 Types:
        1. Completeness Issue: data hai hi nahi
        2. Validity issue: data hai par valid nahi hai. jaise Height negative me.
        3. Accuracy issue: data accurate nahi hai jaise height 2 feet.
        4. Consistency issue: kabhi New York likha hua hai. kabhi NY likha hua hai.
        
          ".ipynb Notebook is made as a implementation of above as 'Assessing_Data' ".   
    

    # Cleaning Data:
    You should follow the order provided below: 
    
        Completeness Issues 
        Tidiness Issues
        Renaming Data Quality issues like validity, accuracy and consistency
        
    # Steps involved in Data cleaning:
        
        Define
        Code
        Test
        
        #always make sure to create a copy of your pandas dataframe before you start the cleaning process.
        
        
        
        
        
      
        
        
        
        
            

       
            
        
3. EDA: There is two step in this step : 
        # Exploring: 
        finding correlation and covarience, uvivariate and mulivariate analysis, plotting graphs.
        
        # Augmenting/ Feature Engineering:
        Changing data by removing outliers
        merging data
        adding new column
        
    
    
4. Drawing conclusions:
    Predict by machine Learning, inferential Statistics and descriptive statistics.
    
5. Communicating Results / Data Storytelling:  
    in person
    Reports
    PPTs / Slides 
    Blog
    
    
    
Fun Fact: These all steps are not Linear. aap kabhi bhi kisi bhi step me jump kar sakte ho. 
     
    
    
    
 
