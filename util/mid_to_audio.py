import IPython.display as ipd
import pretty_midi
import os

def play_midi(midi_path, sr=22050): # notebook only
    if str(type(midi_path)) == "<class 'symusic.core.ScoreTick'>":
        holder_path = "holder.mid"
        midi_path.dump_midi(holder_path)
        midi_path=holder_path
    elif str(type(midi_path)) == "<class 'str'>":
        pass
    fn = os.path.join(midi_path)
    midi_data = pretty_midi.PrettyMIDI(fn)
    
    audio_data = midi_data.synthesize(fs=sr)
    return ipd.Audio(audio_data, rate=sr)