package com.example.demo;

public class FizzBuzz {
    public String play(int number) {
        if (number == 3)
            return "Fizz";
        else if (number == 15)
            return "FizzBuzz";
        else
            return "Buzz";

    }
}
