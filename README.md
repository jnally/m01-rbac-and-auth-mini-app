# Module 1: Assignment - RBAC and Authentication Mini-App
**Author:** Jeremy Nally  
**Course:** SDEV245 - Security and Secure Coding  

## App Logic
This Python script simulates a math testing environment using basic authentication and Role-Based Access Control (RBAC). Upon logging in, users are granted permissions based on their hardcoded role: the `admin` (carl) has exclusive access to view the answer key, while the standard `user` (donut) can only take the test.

## Connection to the CIA Triad
This application demonstrates **Confidentiality**. By restricting the `view_answer_key()` function strictly to the `admin` role, the system ensures that sensitive data (the test answers) remains hidden and completely inaccessible to unauthorized users.

## One-Minute Screen Recording for Module 1: Assignment - RBAC and Authentication Mini-App
[![One-Minute Screen Recording for Module 1: Assignment - RBAC and Authentication Mini-App](https://img.youtube.com/vi/RM5mgDQloeE/maxresdefault.jpg)](https://www.youtube.com/watch?v=RM5mgDQloeE)

## Longer Recording for Module 1: Assignment - RBAC and Authentication Mini-App
[![Longer Recording for Module 1: Assignment - RBAC and Authentication Mini-App](https://img.youtube.com/vi/2g_vrMVNpag/maxresdefault.jpg)](https://www.youtube.com/watch?v=2g_vrMVNpag)
