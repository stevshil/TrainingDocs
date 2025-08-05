package com.tps.myapp.services;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.tps.myapp.entity.Tutorial;
import com.tps.myapp.repository.TutorialRepository;

@Service
public class testServices {

    @Autowired
	TutorialRepository tutorialRepository;

    public List<Tutorial> getAllCds(String title) {
        List<Tutorial> tutorials = new ArrayList<Tutorial>();

        if (title == null)
            tutorialRepository.findAll().forEach(tutorials::add);
        else
            tutorialRepository.findByTitleContaining(title).forEach(tutorials::add);
        
        return tutorials;
    }
}
