package com.example.demo.controler;

import com.example.demo.entity.Book;
import com.example.demo.repostiory.Bookrepostiry;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.List;
@RestController
@RequestMapping("/book")
public class Bookhandleer{
    @Autowired
    private Bookrepostiry bookrepostiry;

    @GetMapping("/findAll")
 public List<Book> findAll()
{

    return  bookrepostiry.findAll();
}


}
