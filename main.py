import json

def find_close_match(user_input, valid_options):
    for option in valid_options:
        if user_input in option or option in user_input:
            return option
    return None

order=[]
total=0

options=['food','drinks','shisha','view','remove','checkout']

print('''
>Hello! Welcome to Al Mokhtar restaurant. 
The place where we bring the vibrant flavors of Lebanon to your table.
''')
with open("menu.json") as file:
    text = file.read()
menu = json.loads(text)

while True:
  choice=input('''------Choose from the following selection----
  1.'food'
  2.'drinks'
  3.'shisha'
  4.'view'
  5.'remove'
  6.'checkout'
  ''').strip().lower()

  if choice not in options:
    match = find_close_match(choice, options)
    if match:
      confirm = input("Did you mean '"+match+"'? (yes/no) ").strip().lower()
      if confirm == 'yes':
        choice = match

  if choice=='food' or choice=='1':
    print("┌─────────────────┐")
    print("│   🍽️  FOOD  🍽️   │")
    print("└─────────────────┘")
    food_menu = menu["food"]
    for category in food_menu:
      print(category.replace("_", " "))
    sub_choice = input("Which category? ").strip().title().replace(" ", "_")

    if sub_choice not in food_menu:
      match = find_close_match(sub_choice, food_menu.keys())
      if match:
        confirm = input("Category not found. Did you mean '"+match.replace("_"," ")+"'? (yes/no) ").strip().lower()
        if confirm == 'yes':
          sub_choice = match
      else:
        print('Category not found')
        sub_choice = None

    if sub_choice in food_menu:
      selected_category = food_menu[sub_choice] 
      if sub_choice == "Appetizers":
        sub_sub_choice = input("Cold or Hot? ").strip().title() + "_Appetizers"
        if sub_sub_choice in selected_category:
          selected_category = selected_category[sub_sub_choice]
        else:
          print("Category not found")
          selected_category = {}
      for item, price in selected_category.items():
        print(item +"- $"+ str(price))
      item_choice = input("Which item would you like? ").title()
      if item_choice in selected_category:
       order.append((item_choice, selected_category[item_choice]))
       print(item_choice+' has been added to your order.')
       total+=selected_category[item_choice]
      else:
       match = find_close_match(item_choice, selected_category.keys())
       if match:
         confirm = input("Item not found. Did you mean '"+match+"'? (yes/no) ").strip().lower()
         if confirm == 'yes':
           order.append((match, selected_category[match]))
           print(match+' has been added to your order.')
           total += selected_category[match]
         else:
           print('item not found')
       else:
         print('item not found')
    
  elif choice=='drinks' or choice=='2':
    print("┌─────────────────┐")
    print("│   🥤 DRINKS 🥤   │")
    print("└─────────────────┘")
    drinks_menu=menu["drinks"]
    for category in drinks_menu:
       print(category.replace("_", " "))
    sub_choice = input("Which category? ").strip().title().replace(" ", "_")

    if sub_choice not in drinks_menu:
      match = find_close_match(sub_choice, drinks_menu.keys())
      if match:
        confirm = input("Category not found. Did you mean '"+match.replace("_"," ")+"'? (yes/no) ").strip().lower()
        if confirm == 'yes':
          sub_choice = match
      else:
        print('Category not found')
        sub_choice = None

    if sub_choice in drinks_menu:
      selected_category = drinks_menu[sub_choice]
      for item, price in selected_category.items():
        print(item +"- $"+ str(price))
      item_choice = input("Which item would you like? ").title()
      if item_choice in selected_category:
        order.append((item_choice, selected_category[item_choice]))
        print(item_choice+' has been added to your order.')
        total += selected_category[item_choice]
      else:
        match = find_close_match(item_choice, selected_category.keys())
        if match:
          confirm = input("Item not found. Did you mean '"+match+"'? (yes/no) ").strip().lower()
          if confirm == 'yes':
            order.append((match, selected_category[match]))
            print(match+' has been added to your order.')
            total += selected_category[match]
          else:
            print('item not found')
        else:
          print('item not found')
      
      
  elif choice=='shisha' or choice=='3':
    print("┌─────────────────┐")
    print("│   💨 SHISHA 💨   │")
    print("└─────────────────┘")
    shisha_menu=menu["shisha"]
    for item, price in shisha_menu.items():
      print(item +"- $"+ str(price))
    item_choice = input("Which item would you like? ").title()
    if item_choice in shisha_menu:
      order.append((item_choice, shisha_menu[item_choice]))
      print(item_choice+' has been added to your order.')
      total=total+shisha_menu[item_choice]
    else:
      match = find_close_match(item_choice, shisha_menu.keys())
      if match:
        confirm = input("Item not found. Did you mean '"+match+"'? (yes/no) ").strip().lower()
        if confirm == 'yes':
          order.append((match, shisha_menu[match]))
          print(match+' has been added to your order.')
          total += shisha_menu[match]
        else:
          print('item not found')
      else:
        print('item not found')
  
  elif choice=='view' or choice=='4':
    print("┌───────────────────┐")
    print("│   🧾  YOUR ORDER  🧾   │")
    print("└───────────────────┘")
    if len(order)>0:
      print('Your order for now (before tax) is:')
      for items,price in order:
       print('==>'+items+'- $'+str(price))
    else:
      print('you  havent ordered anything yet')

  elif choice=='remove' or choice=='5':
    print("┌───────────────────────┐")
    print("│  ❌ REMOVE ITEM ❌   │")
    print("└───────────────────────┘")
    if len(order)>0:
      print('Your current order is:')
      for items,price in order:
        print('==>'+items+'- $'+str(price))
      remove_choice = input("Which item would you like to remove? ").title()
      found = False
      for entry in order:
        if entry[0] == remove_choice:
          order.remove(entry)
          total -= entry[1]
          print(remove_choice+' has been removed from your order.')
          found = True
          break
      if not found:
        print('That item is not in your order.')
    else:
      print('you havent ordered anything yet')
      
  elif choice=='checkout' or choice=='6':
    print("┌────────────────────┐")
    print("│   💳 CHECKOUT 💳    │")
    print("└────────────────────┘")
    tax = total * 0.11
    grand_total = total + tax
    print("your total before tax is: "+str(total))
    print("+11% VAT: "+str(tax))
    print("Total with VAT: "+str(grand_total))
    delivery=input('Would you like them to be delivered to you?(yes/no)').lower()
    answer=['yes','no']
    if delivery==answer[0]:
      location=input("delivery in saida is $4, outside saida is $6. Are you in saida?(yes/no)").lower()
      if location=='yes':
        new_total = total + 4
        new_tax = new_total * 0.11
        print("Before tax: " + str(new_total))
        print("After 11% VAT: " + str(new_total + new_tax))
        print('Enjoy your meal!')
        break
      elif location=='no':
        new_total = total + 6
        new_tax = new_total * 0.11
        print("Before tax: " + str(new_total))
        print("After 11% VAT: " + str(new_total + new_tax))
        print('Enjoy your meal!')
        break
      else:
        print("Please enter either yes or no")
    else:
      print('please enter either yes or no')
      
else:
  print('Choose from the following selection.')