from flask import Flask, request, render_template
app = Flask(__name__)

# Define a function to reverse a number
def reverse_number(num):
    return int(str(num)[::-1])

@app.route('/', methods=['GET', 'POST'])
def reverse():
    if request.method == 'POST':
        number = request.form['number']

        reversed_number = reverse_number(number)

        return f"Reversed number: {reversed_number}"

    return render_template('reverse.html')


if __name__ == '__main__':
    app.run()

class Pet:
    def __init__(self):
        self.accounts = {}
 
    def create_pet(self, pet_id, pet_name):
        
        if not isinstance(pet_id, (int)):
            raise ValueError ("Pet id must be a Integer value")
        elif len(pet_name) < 3:
            raise ValueError ("Pet name must be more than 2 letters.")
        self.accounts[pet_id] = pet_name
        return f'INFO: Succesfully Entered pet data'
 
    def get_pet(self, pet_id):
        if pet_id in self.accounts:
            self.accounts[pet_id]
            return f'INFO: Successfully Fetched Pet Details'
        
        else:
            raise ValueError("Pet_id not found. Please enter correct id")
 
my_Pet = Pet()
try:
    data=my_Pet.create_pet(1, "Dog")
except ValueError as e:
    print(f"Error: {e}")

try:
    my_Pet.create_pet(1, "Do")
except ValueError as e:
    print(f"Error: {e}")

try:
    my_Pet.create_pet("1", "Dog")
except ValueError as e:
    print(f"Error: {e}")

try:
    my_Pet.create_pet(2, "Cat")
except ValueError as e:
    print(f"Error: {e}")

try:
    my_Pet.get_pet(2)
except ValueError as e:
    print(f'Error: {e}')

try:
    my_Pet.get_pet(4)
except ValueError as e:
    print(f'Error: {e}')

