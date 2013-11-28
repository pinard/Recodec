# Conversion of files between different charsets and surfaces.
# -*- coding: utf-8 -*-
# Copyright © 1997, 98, 99, 00, 02 Free Software Foundation, Inc.
# Contributed by François Pinard <pinard@iro.umontreal.ca>, 1997.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with the `recode' Library; see the file `COPYING.LIB'.
# If not, write to the Free Software Foundation, Inc., 59 Temple Place -
# Suite 330, Boston, MA 02111-1307, USA.

import recode

declares = ['Mule']

#    declare_single (outer, "ISO-8859-1", "Mule",
#		    NULL, transform_latin1_mule)
#    && declare_single (outer, "Mule", "ISO-8859-1",
#		       NULL, transform_mule_latin1)
#    && declare_single (outer, "ISO-8859-2", "Mule",
#		       NULL, transform_latin2_mule)
#    && declare_single (outer, "Mule", "ISO-8859-2",

class Action:
    def __init__(self, coding, prefix):
        self.coding = coding
        self.prefix = prefix
        self.codec = None

attempts = [Action('ISO-8859-1', chr(129)),
            Action('ISO-8859-2', chr(130))]

class MuleStep(recode.Step):
    internal_coding = recode.UNICODE_STRING
    external_coding = 'Mule'

    def encode(self, input, errors='strict'):
        output = []
        for character in input:
            unicode = ord(character)
            if unicode < 128:
                output.append(chr(unicode))
        for attempt in attempts:
            if attempt.codec is None:
                attempt.codec = recode.Recodec(
                    '%s..%s' % (recode.UNICODE_STRING, self.coding))
                attempt.codec.encode()


#static bool
#transform_latin_mule (RECODE_SUBTASK subtask,
#		      unsigned prefix)
#{
#  int character;
#
#  while (character = get_byte (subtask), character != EOF)
#    {
#      if (!IS_ASCII (character))
#	put_byte (prefix, subtask);
#      put_byte (character, subtask);
#    }
#  SUBTASK_RETURN (subtask);
#}
#
#static bool
#transform_mule_latin (RECODE_SUBTASK subtask,
#		      unsigned prefix)
#{
#  int character;
#
#  while (character = get_byte (subtask), character != EOF)
#    if (IS_ASCII (character))
#      put_byte (character, subtask);
#    else if ((character & MASK (8)) == prefix)
#      {
#	character = get_byte (subtask);
#
#	while ((character & MASK (8)) == prefix)
#	  {
#	    /* This happens in practice, sometimes, that Emacs goes a bit
#	       berzerk and generates strings of prefix characters.  Remove
#	       all succeeding prefixes in a row.  This is irreversible.  */
#	    RETURN_IF_NOGO (RECODE_NOT_CANONICAL, subtask);
#	    character = get_byte (subtask);
#	  }
#
#	if (character == EOF)
#	  {
#	    RETURN_IF_NOGO (RECODE_INVALID_INPUT, subtask);
#	    break;
#	  }
#
#	if (IS_ASCII (character))
#	  RETURN_IF_NOGO (RECODE_NOT_CANONICAL, subtask);
#	put_byte (character, subtask);
#      }
#    else
#      RETURN_IF_NOGO (RECODE_UNTRANSLATABLE, subtask);
#
#  SUBTASK_RETURN (subtask);
#}
#
##define TRANSFORM_LATIN(To_mule, From_mule, Prefix) \
#									\
#  static bool								\
#  To_mule (RECODE_SUBTASK subtask)	\
#  {									\
#    return transform_latin_mule (subtask, Prefix);			\
#  }									\
#									\
#  static bool								\
#  From_mule (RECODE_SUBTASK subtask)	\
#  {									\
#    return transform_mule_latin (subtask, Prefix);			\
#  }
#
#TRANSFORM_LATIN (transform_latin1_mule, transform_mule_latin1, 129)
#TRANSFORM_LATIN (transform_latin2_mule, transform_mule_latin2, 130)
