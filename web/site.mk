package_name = Recodec
long_package_name = "Recodec sandbox"
rootdir = $(HOME)/entretien/codes/recodec/web
margin_color = "\#f1e4eb"
caption_color = "\#d1b7ff"

SITE_ROOT = 1

TEMPLATE = $(HOME)/entretien/mes-sites/gabarit.html

html-$(host)/recodec.html: src/recodec.html
	@echo "$(package_name) <- $<"
	@$(traiter-html-template-forced)
