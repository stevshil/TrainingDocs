package com.tps.simplecd.repository;

import com.tps.simplecd.model.CompactDisc;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CompactDiscRepository extends JpaRepository<CompactDisc, Long> {
}
