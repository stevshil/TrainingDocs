package com.tps.myapp.services;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.tps.myapp.entity.Book;
import com.tps.myapp.repository.BookRepository;

@Service
public class BookServices {

    @Autowired
	BookRepository bookRepository;

    public List<Book> getAllCds(String title) {
        List<Book> books = new ArrayList<Book>();

        if (title == null)
            bookRepository.findAll().forEach(books::add);
        else
            bookRepository.findByTitleContaining(title).forEach(books::add);
        
        return books;
    }
}
