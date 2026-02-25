package main

import (
	"regexp"
	"strings"
)

var (
	urlRe  = regexp.MustCompile(`(https?://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,}(?:/[^"'\s<>` + "`" + `]*)?)`)
	pathRe = regexp.MustCompile(`["'](\.?\.?/[^"'\s<>` + "`" + `]+)["']`)
	attrRe = regexp.MustCompile(`(?:href|src)=["']([^"']+)["']`)
	robRe  = regexp.MustCompile(`(?i)(?:allow|disallow):\s*(/[^\s]*)`)
	rmapRe = regexp.MustCompile(`(?i)sitemap:\s*(https?://[^\s]*)`)
	smapRe = regexp.MustCompile(`(?i)<loc>\s*([^<\s]+)\s*</loc>`)
)

func extract(c string, re *regexp.Regexp, group int) []string {
	var res []string
	seen := make(map[string]bool)
	for _, m := range re.FindAllStringSubmatch(c, -1) {
		if len(m) > group {
			if s := strings.TrimSpace(m[group]); len(s) > 1 && !strings.ContainsAny(s, "\n ") && !seen[s] {
				seen[s], res = true, append(res, s)
			}
		}
	}
	return res
}

func Extract(c string) (res []string) {
	seen := make(map[string]bool)
	for _, re := range []*regexp.Regexp{urlRe, pathRe, attrRe} {
		for _, v := range extract(c, re, 1) {
			if !seen[v] {
				seen[v], res = true, append(res, v)
			}
		}
	}
	return
}

func ExtractRobots(c string) ([]string, []string) { return extract(c, robRe, 1), extract(c, rmapRe, 1) }
func ExtractSitemap(c string) []string            { return extract(c, smapRe, 1) }
