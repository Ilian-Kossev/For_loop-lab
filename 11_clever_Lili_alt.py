age = int(input())
price_washing_machine = float(input())
price_toy = int(input())
value_toys = 0
sum_money = 0
diminished_money = 0
counter_even_birthdays = 0
number = 1
while number <= age:
    if number % 2 == 1:
        value_toys += price_toy
    else:
        counter_even_birthdays += 1
        sum_money += counter_even_birthdays * 10
        diminished_money += 1
    number += 1
final_sum = value_toys + sum_money - diminished_money
if final_sum >= price_washing_machine:
    remaining_money = final_sum - price_washing_machine
    print(f"Yes! {remaining_money:.2f}")
else:
    missing_money = price_washing_machine - final_sum
    print(f"No! {missing_money:.2f}")
