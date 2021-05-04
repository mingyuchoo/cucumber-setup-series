package com.example.demo;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import io.cucumber.spring.CucumberContextConfiguration;
import org.junit.jupiter.api.Assertions;

@CucumberContextConfiguration
public class FizzBuzzStepdefs {

    FizzBuzz fizzBuzz;
    String result;

    @Given("Create a FizzBuzz game play")
    public void createAFizzBuzzGamePlay() throws Throwable {
        fizzBuzz = new FizzBuzz();
    }

    @When("I play with number {int}")
    public void iPlayWithNumber(int number)  throws Throwable {
        result = fizzBuzz.play(number);
    }

    @Then("The result is {string}")
    public void theResultIs(String resultString) throws Throwable {
        Assertions.assertEquals(result, resultString);
    }
}
