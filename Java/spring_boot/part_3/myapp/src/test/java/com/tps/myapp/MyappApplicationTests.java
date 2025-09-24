package com.tps.myapp;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import java.util.stream.Stream;
import java.util.stream.Collectors;
import java.util.List;
import java.util.Arrays;

// Mockito
import org.junit.jupiter.api.extension.ExtendWith;
import static org.assertj.core.api.Assertions.assertThat;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;


// Our libraries to be tested
import com.tps.myapp.repository.BookRepository;
import com.tps.myapp.services.BookServices;
import com.tps.myapp.entity.Book;


@SpringBootTest
@ExtendWith(MockitoExtension.class)	
class MyappApplicationTests {

	@Mock BookRepository bookDAO;
	@InjectMocks BookServices bookService;

	@Test
	void contextLoads() {
	}

	@Test
	public void testGetAllCds() {
		List<Book> books = Arrays.asList(
			new Book("Book One", "Description One", true),
			new Book("Book Two", "Description Two", false)
		);
		
		when(bookDAO.findAll()).thenReturn(books);

		List<Book> books_get = bookService.getAllCds(null);
		assertThat(books_get instanceof List<Book>).isTrue();
		
		// assertThat(books_get).isNotNull(); //.containsExactly(books);
		assertThat(books_get).containsExactlyElementsOf(books);
		
		verify(bookDAO).findAll();
	}

}
