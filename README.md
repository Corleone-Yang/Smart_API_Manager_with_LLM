# Smart_API_Manager_with_LLM
## 1. Pull the respitory
```
cd /path/to/your/directory  
git clone https://github.com/Corleone-Yang/Smart_API_Manager_with_LLM.git
```
## 2. Set the Environment
```
OPENAI_API_KEY='your_openai_key'
```

## 3. Run the APP
As I have upload the .venv environment, you don't need to create .venv bu your own.
Hence, you can directly run this APP.
```
flask run
```
Note: All the APIs are samples. In the app, we only use their routes and have not actually imported them.

## 4. Sample
### Input:
![Screenshot 2024-07-18 at 20 06 48](https://github.com/user-attachments/assets/5093a713-0dc9-4aa8-8aaa-e6e7021bd5d7)

### Output:
![Screenshot 2024-07-18 at 20 06 09](https://github.com/user-attachments/assets/3d94af0a-c102-4fc0-831c-22d7f1d45bcf)

## 5. Model_Test
You can access the test script by following code.
```
cd Model_Test
python run model.py
```
By this way, you can test the inference classification performance of different models in the ***Smart API Management System***.

Since the frequency of accessing the API within a certain period of time is limited, the test is carried out in two steps.
Here is the test samples for llama3-70B:

![llama3-70B-1](https://github.com/user-attachments/assets/f94b4eb6-8883-49f6-b5f1-3c0618371545)
![llama3-70B-2](https://github.com/user-attachments/assets/cf01e2f6-7205-41f1-b302-ff91c032cdbb)
