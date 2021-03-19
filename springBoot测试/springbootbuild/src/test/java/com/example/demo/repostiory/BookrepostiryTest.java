package com.example.demo.repostiory;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.*;
@SpringBootTest
class BookrepostiryTest {
   @Autowired
   private  Bookrepostiry bookrepostiry;


    @Test
void findAll()
    {
  System.out.println(bookrepostiry.findAll());
    }
}