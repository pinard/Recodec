package_name = Recodec
rootdir = $(HOME)/entretien/codes/web
margin_color = "\#f1e4eb"
caption_color = "\#d1b7ff"

SITE_ROOT = 1

html-$(host)/recodec.html: src/recodec.html
	@echo "$(package_name) ← $<"
	@$(traiter-html-template-forced)
