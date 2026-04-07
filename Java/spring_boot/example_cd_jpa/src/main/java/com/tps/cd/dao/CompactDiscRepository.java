package com.tps.cd.dao;

import com.tps.cd.model.CompactDisc;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CompactDiscRepository extends JpaRepository<CompactDisc, Long> {
}
