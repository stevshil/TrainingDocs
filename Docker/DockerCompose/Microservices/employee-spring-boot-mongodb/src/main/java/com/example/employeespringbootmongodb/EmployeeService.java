package com.example.employeespringbootmongodb;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort.Direction;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public class EmployeeService {

	@Autowired
	private EmployeeRepository repository;
	
	public void doDemo() {
		
		// Insert an employee.
		Employee newEmp = new Employee("Simon Peter", 10000, "Israel");
		repository.save(newEmp);
		System.out.printf("There are now %d employees\n", repository.count());
		
		// Get all employees.
		displayEmployees("All employees after insert: ", repository.findAll());
		
		// Get employees by salary range.
		List<Employee> emps = repository.findEmployeesInSalaryRange(20000,  50000);
		displayEmployees("Employees earning 20k to 50k: ", emps);

		// Get a page of employees.
		Pageable pageable = PageRequest.of(1, 3, Direction.DESC, "dosh");
		Page<Employee> page = repository.findEmployeesByDoshGreaterThan(50000, pageable);
		displayEmployees("Page 1 of employees more than 50k: ", page.getContent());
	}
	
	private void displayEmployees(String message, Iterable<Employee> employees) {
		System.out.printf("\n%s\n", message);
		for (Employee emp: employees) {
			System.out.println(emp);
		}
	}
}
