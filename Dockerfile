FROM node:24-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci --omit=dev

COPY mcp ./mcp
COPY skills ./skills
COPY contracts ./contracts

ENV NODE_ENV=production
ENV HOST=0.0.0.0
ENV PORT=8787
ENV MCP_TRANSPORT=http

EXPOSE 8787

USER node
CMD ["node", "mcp/server.mjs", "--http"]
