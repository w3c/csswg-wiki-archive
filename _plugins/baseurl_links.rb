# Prepend site.baseurl to absolute internal links in rendered HTML.
#
# Links in Markdown sources use root-relative paths like /ideas/foo/.
# When the site is served from a subdirectory (baseurl: /csswg-wiki),
# these need to become /csswg-wiki/ideas/foo/ in the final HTML.
# When baseurl is empty (custom domain), this is a no-op.

Jekyll::Hooks.register [:pages, :documents], :post_render do |item|
  next if item.output_ext != ".html"

  baseurl = item.site.config["baseurl"].to_s
  next if baseurl.empty?

  prefix = Regexp.escape(baseurl.delete_prefix("/"))

  item.output = item.output.gsub(
    /((?:href|src)=")\/(?!#{prefix}\/|\/)/,
    "\\1#{baseurl}/"
  )
end
