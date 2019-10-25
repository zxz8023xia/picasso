# HTML5 runtime
# 
# Copyright (C) 2016 Zhang Ji Peng
# Contact: onecoolx@gmail.com

{
  'variables': {
    'lib_dir': 'libwebp-0.5.1',
    'lib_name': 'webp',
  },
  'target_name': '<(lib_name)',
  'type': 'shared_library',
  'dependencies': [
  ],
  'defines': [
  ],
  'include_dirs': [
    '<(lib_dir)',
  ],
  'sources': [
  '<(lib_dir)/src/dec/alpha.c',
  '<(lib_dir)/src/dec/buffer.c',
  '<(lib_dir)/src/dec/frame.c',
  '<(lib_dir)/src/dec/idec.c',
  '<(lib_dir)/src/dec/io.c',
  '<(lib_dir)/src/dec/quant.c',
  '<(lib_dir)/src/dec/tree.c',
  '<(lib_dir)/src/dec/vp8.c',
  '<(lib_dir)/src/dec/vp8l.c',
  '<(lib_dir)/src/dec/webp.c',
  '<(lib_dir)/src/demux/anim_decode.c',
  '<(lib_dir)/src/demux/demux.c',
  '<(lib_dir)/src/dsp/alpha_processing.c',
  '<(lib_dir)/src/dsp/alpha_processing_mips_dsp_r2.c',
  '<(lib_dir)/src/dsp/alpha_processing_sse2.c',
  '<(lib_dir)/src/dsp/alpha_processing_sse41.c',
  '<(lib_dir)/src/dsp/cpu.c',
  '<(lib_dir)/src/dsp/dec.c',
  '<(lib_dir)/src/dsp/dec_clip_tables.c',
  '<(lib_dir)/src/dsp/dec_mips32.c',
  '<(lib_dir)/src/dsp/dec_mips_dsp_r2.c',
  '<(lib_dir)/src/dsp/dec_msa.c',
  '<(lib_dir)/src/dsp/dec_neon.c',
  '<(lib_dir)/src/dsp/dec_sse2.c',
  '<(lib_dir)/src/dsp/dec_sse41.c',
  '<(lib_dir)/src/dsp/dfilters.c',
  '<(lib_dir)/src/dsp/filters_mips_dsp_r2.c',
  '<(lib_dir)/src/dsp/filters_sse2.c',
  '<(lib_dir)/src/dsp/lossless.c',
  '<(lib_dir)/src/dsp/lossless_mips_dsp_r2.c',
  '<(lib_dir)/src/dsp/lossless_neon.c',
  '<(lib_dir)/src/dsp/lossless_sse2.c',
  '<(lib_dir)/src/dsp/drescaler.c',
  '<(lib_dir)/src/dsp/rescaler_mips32.c',
  '<(lib_dir)/src/dsp/rescaler_mips_dsp_r2.c',
  '<(lib_dir)/src/dsp/rescaler_neon.c',
  '<(lib_dir)/src/dsp/rescaler_sse2.c',
  '<(lib_dir)/src/dsp/upsampling.c',
  '<(lib_dir)/src/dsp/upsampling_mips_dsp_r2.c',
  '<(lib_dir)/src/dsp/upsampling_neon.c',
  '<(lib_dir)/src/dsp/upsampling_sse2.c',
  '<(lib_dir)/src/dsp/yuv.c',
  '<(lib_dir)/src/dsp/yuv_mips32.c',
  '<(lib_dir)/src/dsp/yuv_mips_dsp_r2.c',
  '<(lib_dir)/src/dsp/yuv_sse2.c',
  '<(lib_dir)/src/dsp/argb.c',
  '<(lib_dir)/src/dsp/argb_mips_dsp_r2.c',
  '<(lib_dir)/src/dsp/argb_sse2.c',
  '<(lib_dir)/src/dsp/dcost.c',
  '<(lib_dir)/src/dsp/cost_mips32.c',
  '<(lib_dir)/src/dsp/cost_mips_dsp_r2.c',
  '<(lib_dir)/src/dsp/cost_sse2.c',
  '<(lib_dir)/src/dsp/enc.c',
  '<(lib_dir)/src/dsp/enc_avx2.c',
  '<(lib_dir)/src/dsp/enc_mips32.c',
  '<(lib_dir)/src/dsp/enc_mips_dsp_r2.c',
  '<(lib_dir)/src/dsp/enc_neon.c',
  '<(lib_dir)/src/dsp/enc_sse2.c',
  '<(lib_dir)/src/dsp/enc_sse41.c',
  '<(lib_dir)/src/dsp/lossless_enc.c',
  '<(lib_dir)/src/dsp/lossless_enc_mips32.c',
  '<(lib_dir)/src/dsp/lossless_enc_mips_dsp_r2.c',
  '<(lib_dir)/src/dsp/lossless_enc_neon.c',
  '<(lib_dir)/src/dsp/lossless_enc_sse2.c',
  '<(lib_dir)/src/dsp/lossless_enc_sse41.c',
  '<(lib_dir)/src/enc/ealpha.c',
  '<(lib_dir)/src/enc/analysis.c',
  '<(lib_dir)/src/enc/backward_references.c',
  '<(lib_dir)/src/enc/config.c',
  '<(lib_dir)/src/enc/cost.c',
  '<(lib_dir)/src/enc/delta_palettization.c',
  '<(lib_dir)/src/enc/filter.c',
  '<(lib_dir)/src/enc/eframe.c',
  '<(lib_dir)/src/enc/histogram.c',
  '<(lib_dir)/src/enc/iterator.c',
  '<(lib_dir)/src/enc/near_lossless.c',
  '<(lib_dir)/src/enc/picture.c',
  '<(lib_dir)/src/enc/picture_csp.c',
  '<(lib_dir)/src/enc/picture_psnr.c',
  '<(lib_dir)/src/enc/picture_rescale.c',
  '<(lib_dir)/src/enc/picture_tools.c',
  '<(lib_dir)/src/enc/equant.c',
  '<(lib_dir)/src/enc/syntax.c',
  '<(lib_dir)/src/enc/token.c',
  '<(lib_dir)/src/enc/etree.c',
  '<(lib_dir)/src/enc/evp8l.c',
  '<(lib_dir)/src/enc/webpenc.c',
  '<(lib_dir)/src/mux/anim_encode.c',
  '<(lib_dir)/src/mux/muxedit.c',
  '<(lib_dir)/src/mux/muxinternal.c',
  '<(lib_dir)/src/mux/muxread.c',
  '<(lib_dir)/src/utils/bit_reader.c',
  '<(lib_dir)/src/utils/color_cache.c',
  '<(lib_dir)/src/utils/filters.c',
  '<(lib_dir)/src/utils/huffman.c',
  '<(lib_dir)/src/utils/quant_levels_dec.c',
  '<(lib_dir)/src/utils/random.c',
  '<(lib_dir)/src/utils/rescaler.c',
  '<(lib_dir)/src/utils/thread.c',
  '<(lib_dir)/src/utils/utils.c',
  '<(lib_dir)/src/utils/bit_writer.c',
  '<(lib_dir)/src/utils/huffman_encode.c',
  '<(lib_dir)/src/utils/quant_levels.c',
  '<(lib_dir)/src/extras/extras.c',
  '<(lib_dir)/src/dec/alphai.h',
  '<(lib_dir)/src/dec/common.h',
  '<(lib_dir)/src/dec/decode_vp8.h',
  '<(lib_dir)/src/dec/vp8i.h',
  '<(lib_dir)/src/dec/vp8li.h',
  '<(lib_dir)/src/dec/webpi.h',
  '<(lib_dir)/src/dsp/common_sse2.h',
  '<(lib_dir)/src/dsp/dsp.h',
  '<(lib_dir)/src/dsp/lossless.h',
  '<(lib_dir)/src/dsp/mips_macro.h',
  '<(lib_dir)/src/dsp/msa_macro.h',
  '<(lib_dir)/src/dsp/neon.h',
  '<(lib_dir)/src/dsp/yuv.h',
  '<(lib_dir)/src/enc/backward_references.h',
  '<(lib_dir)/src/enc/cost.h',
  '<(lib_dir)/src/enc/delta_palettization.h',
  '<(lib_dir)/src/enc/histogram.h',
  '<(lib_dir)/src/enc/vp8enci.h',
  '<(lib_dir)/src/enc/vp8li.h',
  '<(lib_dir)/src/mux/muxi.h',
  '<(lib_dir)/src/utils/bit_reader.h',
  '<(lib_dir)/src/utils/bit_reader_inl.h',
  '<(lib_dir)/src/utils/bit_writer.h',
  '<(lib_dir)/src/utils/color_cache.h',
  '<(lib_dir)/src/utils/endian_inl.h',
  '<(lib_dir)/src/utils/filters.h',
  '<(lib_dir)/src/utils/huffman.h',
  '<(lib_dir)/src/utils/huffman_encode.h',
  '<(lib_dir)/src/utils/quant_levels.h',
  '<(lib_dir)/src/utils/quant_levels_dec.h',
  '<(lib_dir)/src/utils/random.h',
  '<(lib_dir)/src/utils/rescaler.h',
  '<(lib_dir)/src/utils/thread.h',
  '<(lib_dir)/src/utils/utils.h',
  '<(lib_dir)/src/webp/format_constants.h',
  '<(lib_dir)/src/webp/decode.h',
  '<(lib_dir)/src/webp/demux.h',
  '<(lib_dir)/src/webp/encode.h',
  '<(lib_dir)/src/webp/mux.h',
  '<(lib_dir)/src/webp/mux_types.h',
  '<(lib_dir)/src/webp/types.h',
  ],
  'conditions': [
    ['OS=="win"', {
      'include_dirs': [
        '$(OutDir)/include',
      ],
      'defines': [
        'WIN32_EXPORT',
        'WEBP_USE_THREAD',
        'HAVE_WINCODEC_H',
      ],
      'actions': [
       {
        'action_name': 'install_header',
        'inputs': [
          '<(lib_dir)/src/webp',
         ],
        'outputs': [
          '$(OutDir)/include/webp',
         ],
        'action': [
          'python',
          'tools/cp.py',
          '<(_inputs)',
          '$(OutDir)/include/webp',
        ],
        'msvs_cygwin_shell': 0,
       },
      ],
    }],
    ['OS=="linux"', {
      'include_dirs': [
        '$(builddir)/include',
      ],
      'defines': [
        'WEBP_USE_THREAD',
      ],
      'cflags': [
        '-fvisibility=hidden',
        '-Wextra -Wold-style-definition',
        '-Wmissing-prototypes',
        '-Wmissing-declarations',
        '-Wdeclaration-after-statement',
        '-Wshadow',
        '-Wformat-security -Wformat-nonliteral',
      ],
      'link_settings': {
        'libraries': [
          '-lpthread',
        ],
      },
      'actions': [
       {
        'action_name': 'install_header',
        'inputs': [
          '<(lib_dir)/src/webp',
        ],
        'outputs': [
          '$(builddir)/include/webp',
        ],
        'action': [
        'python',
        'tools/cp.py',
        '<(_inputs)',
        '$(builddir)/include/webp',
        ],
       },
      ],
    }],
    ['OS=="macosx" or OS=="ios"', {
      'include_dirs': [
        '$(INTERMEDIATE_DIR)/include',
      ],
      'actions': [
       {
        'action_name': 'install_header',
        'inputs': [
          '<(lib_dir)/src/webp/decode.h',
        ],
        'inputs_dir': [
          '<(lib_dir)/src/webp', # gyp macosx issue
        ],
        'outputs': [
          '$(INTERMEDIATE_DIR)/include/webp',
        ],
        'action': [
        'python',
        'tools/cp.py',
        '<(_inputs_dir)',
        '$(INTERMEDIATE_DIR)/include/webp',
        ],
       },
      ],
    }],
  ],
  'includes': [
    '../build/configs.gypi',
    '../build/defines.gypi',
  ],
}

