package com.example.theme.test;

import java.util.ArrayList;
import java.util.List;

/**
 * Test file to demonstrate the CDE Revival Theme syntax highlighting.
 * This file includes various Java language constructs to showcase
 * the theme's color scheme for different code elements.
 * 
 * @author René Schultz Madsen
 * @version 1.0.0
 */
public class ThemeTest {
    
    // Constants - should appear in purple/violet (#5C3C7C)
    private static final String THEME_NAME = "CDE Revival Theme";
    private static final int MAX_ITEMS = 100;
    
    // Instance fields - should appear in blue (#2C4C6C)
    private String name;
    private List<String> items;
    
    /**
     * Constructor demonstrating keywords, types, and strings.
     * 
     * @param name The name parameter
     */
    public ThemeTest(String name) {
        this.name = name;  // 'this' and 'new' are keywords
        this.items = new ArrayList<>();
    }
    
    /**
     * Method declaration to show function highlighting.
     * Keywords like 'public', 'void', 'if', 'else', 'return' should be bold.
     * 
     * @param value An integer value
     * @return true if the value is valid
     */
    public boolean addItem(int value) {
        // Comments should appear in grey and italic (#5C6574)
        if (value > MAX_ITEMS) {
            System.err.println("Error: Value exceeds maximum");  // Error output
            return false;
        } else if (value < 0) {
            System.out.println("Warning: Negative value");  // Standard output
            return false;
        }
        
        // String literals should be green (#2C6C3C)
        String item = "Item #" + value;
        items.add(item);
        
        return true;
    }
    
    /**
     * Demonstrates various operators and numeric literals.
     */
    public void demonstrateOperators() {
        // Numeric literals - should appear in purple (#5C3C7C)
        int decimal = 42;
        double floating = 3.14159;
        long bigNumber = 1234567890L;
        
        // Mathematical operators
        int result = decimal + 10 - 5 * 2 / 3;
        boolean comparison = (result > 0) && (result < 100) || (result == 42);
        
        // Bitwise operators
        int bitwise = decimal & 0xFF | 0x10 ^ 0x05;
    }
    
    /**
     * Shows lambda expressions and streams (Java 8+).
     */
    public void modernJavaFeatures() {
        items.stream()
            .filter(item -> item.length() > 5)
            .map(String::toUpperCase)
            .forEach(System.out::println);
    }
    
    /**
     * Deprecated method to show strikethrough styling.
     * 
     * @deprecated Use {@link #addItem(int)} instead
     */
    @Deprecated
    public void oldMethod() {
        // This method is deprecated
    }
    
    /**
     * TODO: This shows a TODO comment highlight
     * FIXME: And this is a FIXME highlight
     */
    public void todoExample() {
        // Regular comment without special markers
    }
    
    /**
     * Main method for testing.
     */
    public static void main(String[] args) {
        ThemeTest test = new ThemeTest("CDE Theme Test");
        
        // Loop structures
        for (int i = 0; i < 10; i++) {
            test.addItem(i);
        }
        
        // Enhanced for loop
        for (String item : test.items) {
            System.out.println("Item: " + item);
        }
        
        // Exception handling
        try {
            test.modernJavaFeatures();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            System.out.println("Done!");
        }
    }
}
