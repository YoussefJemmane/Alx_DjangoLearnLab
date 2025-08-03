#!/usr/bin/env python3
"""
Test script for the Django REST Framework API
This script demonstrates how to interact with the API endpoints
"""

import requests
import json

# API base URL
BASE_URL = 'http://127.0.0.1:8000/api'

def get_auth_token(username, password):
    """Get authentication token for API access"""
    url = f'{BASE_URL}/auth/token/'
    data = {'username': username, 'password': password}
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            token = response.json()['token']
            print(f"✅ Authentication successful. Token: {token}")
            return token
        else:
            print(f"❌ Authentication failed: {response.status_code}")
            print(response.text)
            return None
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Make sure the Django server is running.")
        return None

def test_book_endpoints(token):
    """Test all book-related endpoints"""
    headers = {'Authorization': f'Token {token}'}
    
    print("\n📚 Testing Book Endpoints")
    print("=" * 50)
    
    # 1. List all books (ListAPIView)
    print("\n1. Testing BookList endpoint (GET /api/books/)")
    response = requests.get(f'{BASE_URL}/books/', headers=headers)
    if response.status_code == 200:
        books = response.json()
        print(f"✅ Found {len(books)} books via BookList endpoint")
        for book in books[:2]:  # Show first 2 books
            print(f"   - {book['title']} by {book['author']}")
    else:
        print(f"❌ BookList failed: {response.status_code}")
    
    # 2. List all books (ViewSet)
    print("\n2. Testing BookViewSet endpoint (GET /api/books_all/)")
    response = requests.get(f'{BASE_URL}/books_all/', headers=headers)
    if response.status_code == 200:
        books = response.json()
        print(f"✅ Found {len(books)} books via BookViewSet endpoint")
        for book in books[:2]:  # Show first 2 books
            print(f"   - {book['title']} by {book['author']}")
    else:
        print(f"❌ BookViewSet list failed: {response.status_code}")
    
    # 3. Create a new book
    print("\n3. Testing book creation (POST /api/books_all/)")
    new_book = {
        'title': 'Test-Driven Development with Python',
        'author': 'Harry Percival'
    }
    response = requests.post(f'{BASE_URL}/books_all/', headers=headers, json=new_book)
    if response.status_code == 201:
        created_book = response.json()
        book_id = created_book['id']
        print(f"✅ Created book with ID {book_id}: {created_book['title']}")
        
        # 4. Retrieve the specific book
        print(f"\n4. Testing book retrieval (GET /api/books_all/{book_id}/)")
        response = requests.get(f'{BASE_URL}/books_all/{book_id}/', headers=headers)
        if response.status_code == 200:
            book = response.json()
            print(f"✅ Retrieved book: {book['title']} by {book['author']}")
        else:
            print(f"❌ Book retrieval failed: {response.status_code}")
        
        # 5. Update the book
        print(f"\n5. Testing book update (PUT /api/books_all/{book_id}/)")
        updated_book = {
            'title': 'Test-Driven Development with Python (Updated)',
            'author': 'Harry Percival (Updated)'
        }
        response = requests.put(f'{BASE_URL}/books_all/{book_id}/', headers=headers, json=updated_book)
        if response.status_code == 200:
            book = response.json()
            print(f"✅ Updated book: {book['title']}")
        else:
            print(f"❌ Book update failed: {response.status_code}")
        
        # 6. Delete the book
        print(f"\n6. Testing book deletion (DELETE /api/books_all/{book_id}/)")
        response = requests.delete(f'{BASE_URL}/books_all/{book_id}/', headers=headers)
        if response.status_code == 204:
            print(f"✅ Deleted book with ID {book_id}")
        else:
            print(f"❌ Book deletion failed: {response.status_code}")
    else:
        print(f"❌ Book creation failed: {response.status_code}")
        print(response.text)

def test_without_authentication():
    """Test API access without authentication"""
    print("\n🔒 Testing Authentication Requirements")
    print("=" * 50)
    
    print("\nTesting access without authentication token...")
    response = requests.get(f'{BASE_URL}/books/')
    if response.status_code == 401:
        print("✅ Correctly denied access without authentication")
    else:
        print(f"❌ Unexpected response: {response.status_code}")

def main():
    """Main test function"""
    print("🚀 Django REST Framework API Test")
    print("=" * 50)
    
    # Test without authentication first
    test_without_authentication()
    
    # Get authentication token
    print("\n🔐 Getting Authentication Token")
    print("=" * 50)
    token = get_auth_token('admin', 'admin123')
    
    if token:
        # Test all endpoints with authentication
        test_book_endpoints(token)
        
        print("\n🎉 All tests completed!")
        print("=" * 50)
    else:
        print("❌ Cannot proceed without authentication token")

if __name__ == '__main__':
    print("Make sure the Django server is running: python manage.py runserver")
    print("Press Enter to continue or Ctrl+C to cancel...")
    input()
    main()
