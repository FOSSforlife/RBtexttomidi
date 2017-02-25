from reaper_python import *

RPR_ShowConsoleMsg("")


def msg(param):
	RPR_ShowConsoleMsg(param)
	RPR_ShowConsoleMsg("\n")
	return

def getActTakeInEditor():
	return RPR_MIDIEditor_GetTake(RPR_MIDIEditor_GetActive())
	
def getStartPPQ(num): #if someone could help me simplify this, that would be great. still learning python/reascript
	take = getActTakeInEditor()
	(retval, take, noteidx, sel, mute, startppq, endppq, chan, pitch, vel) = RPR_MIDI_GetNote(take, num, 0, 0, 0, 0, 0, 0, 0) #get startppq
	return startppq

def convertPitch(note, diff): #converts from text note (1-5) to correct MIDI pitch 
	noteint = ord(note)
	if diff == 'x':
		return noteint + 47
	elif diff == 'h':
		return noteint + 35
	elif diff == 'm':
		return noteint + 23
	elif diff == 'e':
		return noteint + 11
	else:
		return noteint + 47
	
def addNote(take, startpos, note):
	pitch = convertPitch(note, 'x')
	endpos = startpos + 120
	RPR_MIDI_InsertNote(take, 1, 0, startpos, endpos, 0, pitch, 96, 0)
	return 

def findPreviousNote(take, ppq):
	(ok, take, notes, ccs, sysex) = RPR_MIDI_CountEvts(take, 0, 0, 0)
	for num in range(0, notes):
		startppq = getStartPPQ(num)
		if startppq >= ppq:
			return num - 1;
	
def extendNote(take, length, start):
	prevNoteid = findPreviousNote(take, start)
	startppq = getStartPPQ(prevNoteid)
	RPR_MIDI_SetNote(take, prevNoteid, -1, 0, -1, startppq + length, -1, -1, -1, -1)
	return
	
def addNotesFromStr(take, meas, beat, strn):
	curPos = (meas-1) * 960 + (beat-1)*480
	lengthCount = 120
	for num in strn: #for each digit/character
		if lengthCount > 120: 
			if ord(num) != 45:
				extendNote(take, lengthCount, curPos)
				lengthCount = 120
		if ord(num) > 48 and ord(num) < 54: # 1-5
			addNote(take, curPos, num)
		elif ord(num) == 120: # 'x'
			pass
		elif ord(num) == 45: # '-'
			lengthCount += 120
		curPos += 120
		
	return
	
def main():
	take = getActTakeInEditor()
	addNotesFromStr(take, 5, 1, "21-x21-x231-x2341-x31-x4")

main()
