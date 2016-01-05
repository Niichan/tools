package cqbot

import "strings"

// IRC line
type Line struct {
	Source string
	Verb   string
	Args   []string
}

// Create a new line and split out an RFC 1459 frame to a Line
func NewLine(input string) (line *Line) {
	line = &Line{}

	split := strings.Split(input, " ")

	if split[0][0] == ':' {
		line.Source = split[0][1:]
		line.Verb = split[1]
		split = split[2:]
	} else {
		line.Source = ""
		line.Verb = split[0]
		split = split[1:]
	}

	argstring := strings.Join(split, " ")
	extparam := strings.Split(argstring, " :")

	if len(extparam) > 1 {
		ext := strings.Join(extparam[1:], " :")
		args := strings.Split(extparam[0], " ")

		line.Args = append(args, ext)
	} else {
		line.Args = split
	}

	return
}
