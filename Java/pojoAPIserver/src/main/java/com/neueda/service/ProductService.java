package com.neueda.service;

import com.neueda.model.Product;
import com.neueda.repository.ProductRepository;

import java.sql.SQLException;
import java.util.List;
import java.util.Optional;

public class ProductService {

    private final ProductRepository repository;

    public ProductService(ProductRepository repository) {
        this.repository = repository;
    }

    // -------------------------
    // Get all products
    // -------------------------
    public List<Product> getAllProducts() throws SQLException {
        return repository.findAll();
    }

    // -------------------------
    // Get product by ID
    // -------------------------
    public Optional<Product> getProductById(int id) throws SQLException {
        return repository.findById(id);
    }

    // -------------------------
    // Create new product
    // -------------------------
    public Product createProduct(Product product) throws SQLException {
        validateProduct(product);
        return repository.insert(product);
    }

    // -------------------------
    // Update existing product
    // -------------------------
    public Product updateProduct(Product product) throws SQLException {
        validateProduct(product);
        return repository.update(product);
    }

    // -------------------------
    // Save (insert or update)
    // -------------------------
    public Product save(Product product) throws SQLException {
        validateProduct(product);
        return repository.save(product);
    }

    // -------------------------
    // Delete product
    // -------------------------
    public boolean deleteProduct(int id) throws SQLException {
        return repository.delete(id);
    }

    // -------------------------
    // Validation logic
    // -------------------------
    private void validateProduct(Product product) {
        if (product.getName() == null || product.getName().isBlank()) {
            throw new IllegalArgumentException("Product name cannot be empty");
        }
        if (product.getPrice() < 0) {
            throw new IllegalArgumentException("Price cannot be negative");
        }
    }
}
