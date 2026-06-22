# Quickstart: Skills Site (Next.js)

## Prerequisites
- Node.js 20+
- Docker (optional)

## Setup & Run Locally
1. Install dependencies:
   ```bash
   npm install
   ```
2. Link Vercel project (if needed for the OIDC token):
   ```bash
   vercel link
   vercel env pull
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```
4. Open [http://localhost:3000](http://localhost:3000).

## Run with Docker
1. Build the image:
   ```bash
   docker build -t skills-app .
   ```
2. Run the container:
   ```bash
   docker run -p 3000:3000 -e VERCEL_OIDC_TOKEN=your_token skills-app
   ```
