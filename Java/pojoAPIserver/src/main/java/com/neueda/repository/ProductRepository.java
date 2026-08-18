package com.neueda.repository;

import com.neueda.model.Product;

import javax.sql.DataSource;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class ProductRepository {
    private final DataSource dataSource;

    public ProductRepository(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    // -------------------------
    // findAll()
    // -------------------------
    public List<Product> findAll() throws SQLException {
        String sql = "SELECT * FROM products";
        List<Product> products = new ArrayList<>();

        try (Connection conn = dataSource.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()) {

            while (rs.next()) {
                products.add(mapRow(rs));
            }
        }
        return products;
    }

    // -------------------------
    // findById()
    // -------------------------
    public Optional<Product> findById(int id) throws SQLException {
        String sql = "SELECT id, name, price FROM products WHERE id = ?";

        try (Connection conn = dataSource.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id);

            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    return Optional.of(mapRow(rs));
                }
            }
        }
        return Optional.empty();
    }

    // -------------------------
    // INSERT
    // -------------------------
    public Product insert(Product product) throws SQLException {
        String sql = "INSERT INTO products (name, price) VALUES (?, ?)";

        try (Connection conn = dataSource.getConnection();
             PreparedStatement stmt = conn.prepareStatement(
                     sql, Statement.RETURN_GENERATED_KEYS)) {

            stmt.setString(1, product.getName());
            stmt.setDouble(2, product.getPrice());
            stmt.executeUpdate();

            try (ResultSet keys = stmt.getGeneratedKeys()) {
                if (keys.next()) {
                    product.setId(keys.getInt(1));
                }
            }
        }
        return product;
    }

    // -------------------------
    // UPDATE
    // -------------------------
    public Product update(Product product) throws SQLException {
        String sql = "UPDATE products SET name = ?, price = ? WHERE id = ?";

        try (Connection conn = dataSource.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, product.getName());
            stmt.setDouble(2, product.getPrice());
            stmt.setInt(3, product.getId());
            stmt.executeUpdate();
        }
        return product;
    }

    // -------------------------
    // SAVE (delegates)
    // -------------------------
    public Product save(Product product) throws SQLException {
        return product.getId() == 0
                ? insert(product)
                : update(product);
    }

    // -------------------------
    // Row mapper
    // -------------------------
    private Product mapRow(ResultSet rs) throws SQLException {
        return new Product(
                rs.getInt("id"),
                rs.getString("name"),
                rs.getDouble("price")
        );
    }

    public boolean delete(int id) throws SQLException {
        String sql = "DELETE FROM products WHERE id = ?";

        try (Connection conn = dataSource.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, id);
            int rows = stmt.executeUpdate();
            return rows > 0;
        }
    }

}
