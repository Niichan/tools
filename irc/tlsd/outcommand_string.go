// generated by stringer -type=OutCommand; DO NOT EDIT

package main

import "fmt"

const _OutCommand_name = "CommandOutNoneCommandOutIAmUselessCommandOutNoSSLCommandOutInvalidKeysCommandOutStatsCommandOutFingerprintCommandOutCloseConnCommandOutNoZlib"

var _OutCommand_index = [...]uint8{0, 14, 34, 49, 70, 85, 106, 125, 141}

func (i OutCommand) String() string {
	if i < 0 || i+1 >= OutCommand(len(_OutCommand_index)) {
		return fmt.Sprintf("OutCommand(%d)", i)
	}
	return _OutCommand_name[_OutCommand_index[i]:_OutCommand_index[i+1]]
}