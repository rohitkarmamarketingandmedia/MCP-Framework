#!/usr/bin/env python3
"""
MCP Framework Local Test Script
Tests all endpoints without running full server
"""

import sys
sys.path.insert(0, '/home/claude/mcp-framework')

from app import app
import json

def test_endpoint(client, method, path, data=None):
    """Test an endpoint and return formatted result"""
    print(f"\n{'='*60}")
    print(f"Testing: {method} {path}")
    print('='*60)
    
    if method == 'GET':
        response = client.get(path)
    else:
        response = client.post(path, 
                              json=data,
                              content_type='application/json')
    
    print(f"Status: {response.status_code}")
    print(f"Response:")
    
    try:
        result = response.get_json()
        print(json.dumps(result, indent=2))
        return result
    except:
        print(response.data.decode())
        return None

def main():
    """Run all endpoint tests"""
    print("\n" + "="*60)
    print("MCP FRAMEWORK - LOCAL TEST SUITE")
    print("="*60)
    
    with app.test_client() as client:
        
        # Test 1: Health Check
        print("\n[TEST 1] Health Check")
        health = test_endpoint(client, 'GET', '/health')
        assert health['status'] == 'healthy', "Health check failed!"
        print("✅ Health check passed")
        
        # Test 2: Home/API Docs
        print("\n[TEST 2] Home/API Documentation")
        home = test_endpoint(client, 'GET', '/')
        assert 'agents' in home, "Home endpoint missing agents info!"
        print("✅ Home endpoint passed")
        
        # Test 3: Generate Relo Kit (Core functionality)
        print("\n[TEST 3] Generate EDC Relo Kit")
        kit_data = {
            "keyword": "VR Relos Sarasota",
            "quote": "play here, build here",
            "geo": "Sarasota"
        }
        kit = test_endpoint(client, 'POST', '/generate_relo_kit', kit_data)
        assert kit['status'] == 'success', "Kit generation failed!"
        assert 'blog' in kit['outputs'], "Missing blog output!"
        assert 'schema' in kit['outputs'], "Missing schema output!"
        assert 'social_kit' in kit['outputs'], "Missing social kit!"
        assert 'report' in kit['outputs'], "Missing report!"
        print("✅ Relo kit generation passed")
        
        # Test 4: EDC Metrics Dashboard
        print("\n[TEST 4] EDC Metrics Dashboard")
        metrics = test_endpoint(client, 'GET', '/edc_metrics')
        assert 'metrics' in metrics, "Missing metrics!"
        assert 'revenue' in metrics, "Missing revenue forecast!"
        print("✅ Metrics dashboard passed")
        
    print("\n" + "="*60)
    print("ALL TESTS PASSED! ✅")
    print("="*60)
    print("\nMCP Framework is ready for Render deployment!")
    print("\nNext steps:")
    print("1. Push code to GitHub")
    print("2. Deploy to Render.com")
    print("3. Test live URL")
    print("4. Proceed to Day 2 (EDC MVP enhancements)")

if __name__ == '__main__':
    main()
