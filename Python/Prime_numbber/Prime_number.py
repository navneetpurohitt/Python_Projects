import streamlit as st

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    st.title("Prime Number Checker")
    st.write("Enter a number to check if it is a prime number.")

    number = st.number_input("Enter a number:", min_value=0, step=1)

    if st.button("Check"):
        if is_prime(number):
            st.success(f"{number} is a prime number!")
        else:
            st.error(f"{number} is not a prime number.")

if __name__ == "__main__":
    main()