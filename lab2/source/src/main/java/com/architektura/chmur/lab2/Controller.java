package com.architektura.chmur.lab2;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

@RestController
public class Controller {

    @GetMapping
    public String helloWorld() {
        return "Hello World";
    }

    @GetMapping(path = "/time")
    public String time() {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("HH:mm:ss");
        ZoneId zoneId = ZoneId.of("Europe/Warsaw");
        ZonedDateTime now = LocalDateTime.now().atZone(zoneId);
        return dtf.format(now);
    }

    @GetMapping(path = "/rev/{text}")
    public String reverseString(@PathVariable String text) {
        return new StringBuilder(text).reverse().toString();
    }
}
