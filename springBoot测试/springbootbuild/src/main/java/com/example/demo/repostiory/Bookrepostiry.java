package com.example.demo.repostiory;

import com.example.demo.entity.Book;
import org.springframework.data.jpa.repository.JpaRepository;

public interface Bookrepostiry extends JpaRepository<Book,Integer>{


}
