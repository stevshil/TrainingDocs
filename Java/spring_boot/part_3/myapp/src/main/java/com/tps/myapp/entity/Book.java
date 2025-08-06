package com.tps.myapp.entity;

// import javax.persistence.*;
import jakarta.persistence.*; // for Spring Boot 3
import lombok.*;

@Entity
@Getter	// From lombok - saves defining them
@Setter	// From lombok
@Table(name = "books")
public class Book {

	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	private long id;

	@Column(name = "title")
	private String title;

	@Column(name = "description")
	private String description;

	@Column(name = "published")
	private boolean published;

	public Book() {

	}

	public Book(String title, String description, boolean published) {
		this.title = title;
		this.description = description;
		this.published = published;
	}

	@Override
	public String toString() {
		return "Tutorial [id=" + id + ", title=" + title + ", desc=" + description + ", published=" + published + "]";
	}

}