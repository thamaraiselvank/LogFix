package com.charan.homepageappspringbootjar.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class AppController {

	@RequestMapping("/")
	public String loadHomepage() {
		return "index";
	}
	@RequestMapping("/admin")
    	public String adminPage() {
        return "admin";
    	}
	
}
