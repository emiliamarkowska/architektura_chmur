package com.architektura.chmur.lab2;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

@RestController
public class Controller {

    @GetMapping
    public String server(@RequestParam(required = false) String cmd, @RequestParam(required = false) String str) throws Exception {
        if (cmd == null) {
            return helloWorld();
        }
        if (cmd.equals("time") && str == null) {
            return time();
        }

        if (cmd.equals("rev") && str != null) {
            return reverseString(str);
        }
        throw new Exception();
    }

    private String helloWorld() {
        return "Hello World";
    }


    private String time() {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("HH:mm:ss");
        ZoneId zoneId = ZoneId.of("Europe/Warsaw");
        ZonedDateTime now = LocalDateTime.now().atZone(zoneId);
        return dtf.format(now);
    }

    private String reverseString(String text) {
        return new StringBuilder(text).reverse().toString();
    }

}
