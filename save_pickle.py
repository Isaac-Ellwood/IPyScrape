import pickle

try:
    # Deserialize the object from the binary file
    with open('data.pkl', 'rb') as file:
        loaded_data = pickle.load(file)
        data = loaded_data
except:
    # Initialise empty list
    data = []

print (data)

titleText = "title"
bodyText = "body"
authorText = "no author"

def save_data():
    # Append list
    data.append([titleText, authorText, bodyText])
    # Serialize the object to a binary format
    with open('data.pkl', 'wb') as file:
        pickle.dump(data, file)

save_data()

# Deserialize the object from the binary file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)