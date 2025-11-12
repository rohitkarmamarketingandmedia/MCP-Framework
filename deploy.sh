#!/bin/bash
# MCP Framework - Render Quick Deploy Script
# Run this after pushing code to GitHub

echo "=================================================="
echo "MCP FRAMEWORK - RENDER QUICK DEPLOY"
echo "=================================================="
echo ""

# Check if GitHub CLI is available
if command -v gh &> /dev/null; then
    echo "✅ GitHub CLI detected"
    echo "Creating repository..."
    gh repo create mcp-framework --public --description "MCP Framework - EDC Innovation Engine" --source=. --push
    echo "✅ Repository created and pushed!"
else
    echo "⚠️  GitHub CLI not found. Manual steps required:"
    echo ""
    echo "1. Create new repo on GitHub: mcp-framework"
    echo "2. Run these commands:"
    echo "   git init"
    echo "   git add ."
    echo "   git commit -m 'Initial MCP Framework deployment'"
    echo "   git branch -M main"
    echo "   git remote add origin https://github.com/YOUR-USERNAME/mcp-framework.git"
    echo "   git push -u origin main"
    echo ""
fi

echo ""
echo "=================================================="
echo "NEXT: DEPLOY TO RENDER"
echo "=================================================="
echo ""
echo "1. Go to: https://dashboard.render.com/"
echo "2. Click 'New +' → 'Web Service'"
echo "3. Connect your GitHub repo: mcp-framework"
echo "4. Configure:"
echo "   - Build Command: pip install -r requirements.txt"
echo "   - Start Command: gunicorn app:app"
echo "   - Plan: Free (or Starter $7/mo)"
echo ""
echo "5. Add Environment Variables:"
echo "   OPENAI_API_KEY = sk-your-key (optional)"
echo "   WP_BASE_URL = https://demo.wp.com"
echo ""
echo "6. Click 'Create Web Service'"
echo "7. Wait 3-5 minutes for deployment"
echo ""
echo "8. Test your live URL:"
echo "   curl https://YOUR-APP.onrender.com/health"
echo ""
echo "=================================================="
echo "ESTIMATED TIME: 15 minutes"
echo "=================================================="
echo ""
echo "Questions? Check README.md for detailed guide"
echo ""
