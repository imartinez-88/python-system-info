# Refactoring 

## Original Project python-demo-app 
- Full AWS EC2 deployment with SSH keys 
- Gitlab CI/CD with docker-in-docker connection 
- Manual secret managment 
- Flask + Jinja template issues

# Improvments made in this version: 

### Infrastructure Simplification
- **Removed**: AWS EC2, SSH keys, cloud deployment
- **Added**: Local Docker Compose, development-friendly setup
- **Why**: Faster iteration, no cloud costs for learning

### CI/CD Migration
- **From**: GitLab `.gitlab-ci.yml`
- **To**: GitHub Actions `.github/workflows/ci.yml`
- **Why**: Better marketplace integrations, cleaner syntax

### Features Added
1. Real-time dashboard with gradient UI
2. Detailed system metrics (CPU, memory, disk, uptime)
3. Optional Prometheus + Grafana monitoring
4. Multi-stage Docker builds (reduced image size)

### What I Learned
- GitHub Actions caches dependencies better than GitLab runners
- Docker Compose for local dev is more reproducible than EC2
- Multi-stage builds reduced image from ~900MB to ~150MB
- Flask's `render_template` requires specific folder structure