# MCP Framework - Render Deployment Guide

## Day 1: Deploy to Render.com (15 minutes)

### Prerequisites
- Render.com account (free tier works)
- GitHub account (to push code)
- OpenAI API key (optional for demo - works with placeholder)

### Step 1: Push Code to GitHub (5 min)

1. Create new GitHub repo: `mcp-framework`
2. Upload these files from `/home/claude/mcp-framework/`:
   - `app.py`
   - `requirements.txt`
   - `render.yaml`
   - `README.md` (this file)

```bash
git init
git add .
git commit -m "Initial MCP Framework deployment"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/mcp-framework.git
git push -u origin main
```

### Step 2: Deploy on Render (10 min)

1. **Go to Render Dashboard**: https://dashboard.render.com/
2. **New Web Service**: Click "New +" → "Web Service"
3. **Connect Repository**: 
   - Connect your GitHub account
   - Select `mcp-framework` repo
   - Click "Connect"

4. **Configure Service**:
   - **Name**: `mcp-framework` (or custom)
   - **Region**: Oregon (US West) or closest
   - **Branch**: `main`
   - **Root Directory**: Leave blank
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free (or Starter $7/mo for better performance)

5. **Environment Variables** (Add in "Environment" section):
   ```
   OPENAI_API_KEY = sk-your-actual-key-here
   WP_BASE_URL = https://demo.wp.com
   SEMRUSH_API_KEY = your-semrush-key
   GBP_LOCATION_ID = 123
   GA4_PROPERTY_ID = your-ga4-id
   ```
   
   **For demo/testing**: Leave OPENAI_API_KEY as placeholder - the app will work with template content.

6. **Deploy**: Click "Create Web Service"
   - Render will build and deploy (3-5 minutes)
   - Watch logs in real-time

### Step 3: Test Deployment (5 min)

Once deployed, your URL will be: `https://mcp-framework-XXXX.onrender.com`

#### Test 1: Health Check
```bash
curl https://YOUR-APP.onrender.com/health
```

Expected response:
```json
{
  "status": "healthy",
  "mcp_ready": true,
  "hosting": "render-stable",
  "version": "1.0-fresh-claude"
}
```

#### Test 2: Generate Relo Kit
```bash
curl -X POST https://YOUR-APP.onrender.com/generate_relo_kit \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "VR Relos Sarasota",
    "quote": "play here, build here",
    "geo": "Sarasota"
  }'
```

Expected response: JSON with blog, schema, social_kit, report

#### Test 3: EDC Metrics Dashboard
```bash
curl https://YOUR-APP.onrender.com/edc_metrics
```

Expected response: Dashboard metrics with revenue forecast

### Step 4: Capture Day 1 Output

**Required Deliverables**:
1. ✅ Live Render URL: `https://mcp-framework-XXXX.onrender.com`
2. ✅ Health check screenshot showing "healthy" status
3. ✅ Test of `/generate_relo_kit` with VR Relos input
4. ✅ Response JSON showing blog, schema, social kit, metrics

### Troubleshooting

**Build Fails**:
- Check Build Logs in Render dashboard
- Verify requirements.txt has all dependencies
- Ensure Python 3.11 is set

**App Won't Start**:
- Check Deploy Logs for errors
- Verify start command: `gunicorn app:app`
- Check PORT environment variable (Render sets automatically)

**502 Bad Gateway**:
- App is deploying - wait 30 seconds
- Check logs for Python errors
- Verify Flask is binding to `0.0.0.0` and PORT

**Missing Environment Variables**:
- Double-check all keys are added in Render dashboard
- Redeploy after adding variables

### Alternative: Test Locally First

```bash
cd /home/claude/mcp-framework
pip install -r requirements.txt
export OPENAI_API_KEY=sk-placeholder
python app.py
```

Then test: `http://localhost:5000/health`

---

## Day 1 Complete Checklist

- [ ] Code pushed to GitHub
- [ ] Render service created and deployed
- [ ] Health check returns "healthy"
- [ ] `/generate_relo_kit` generates complete kit
- [ ] Live URL captured: __________________
- [ ] Screenshot of working endpoint saved

**Next**: Proceed to Day 2 (EDC MVP enhancements)

---

## Quick Reference

**Endpoints**:
- `GET /` - Home/API docs
- `GET /health` - Health check
- `POST /generate_relo_kit` - Generate complete EDC kit
- `GET /edc_metrics` - Dashboard metrics

**Architecture**:
- Flask backend (Python 3.11)
- Gunicorn WSGI server
- Modular agent design (Content, Schema, Social, Report)
- JSON API responses
- Ready for n8n integration

**Revenue Model**:
- EDC Subscription: $2K/mo base
- Relo Kits: $750 each × 20/mo = $15K
- Monthly Target: $17K
- Annual Projection: $204K

**Mission**: Deploy EDC Innovation Engine → Demo to Erin → Scale to $100K/mo
