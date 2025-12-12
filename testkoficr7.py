# write a program that helps check if a movie is suitable for a person based on their age
#and the movie's age rating category.



age = int(input("Enter your age: "))
if age > 18:
    print("You can watch any movie (including adult-rated).")
elif age >= 13:
    print("You can watch PG-13 and below rated movies.")
elif age >= 7:
    print("You can watch G and PG below rated movies.")        
else :
    print("You can only watch G rated (General audiences) movies.")