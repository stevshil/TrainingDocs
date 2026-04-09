package com.tps.multidbcdlibrary.repository;

import com.tps.multidbcdlibrary.model.CompactDisc;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CompactDiscRepository extends JpaRepository<CompactDisc, Long> {
}
