package com.tps.myapp.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import com.tps.myapp.entity.*;

public interface TutorialRepository extends JpaRepository<Tutorial, Long> {
  List<Tutorial> findByPublished(boolean published);

  List<Tutorial> findByTitleContaining(String title);
}